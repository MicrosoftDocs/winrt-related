---
author: stevewhims
description: An introduction to Microsoft Interface Definition Language 3.0.
title: Introduction to Microsoft Interface Definition Language 3.0
ms.author: stwhi
ms.date: 04/23/2018
ms.topic: reference
keywords: windows 10, uwp, winrt, api, reference, idl, midl, 3.0, 3, midl3
ms.localizationpriority: medium
---

# Introduction to Microsoft Interface Definition Language 3.0
Microsoft Interface Definition Language (MIDL) 3.0 is a simplified, modern syntax for defining Windows Runtime types inside Interface Definition Language (IDL) files (`.idl` files). This new syntax will feel familiar to anyone experienced with C, C++, C#, and/or Java. MIDL 3.0 is a particularly convenient way to define [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/index) runtime classes, being dramatically more concise than previous versions of IDL (reducing designs by two thirds in length, and using reasonable defaults to reduce the need for decorating with attributes).

Here's how MIDL 3.0 looks; this example demonstrates most of the language syntax elements that you'll likely use.

```idl
// Photo.idl
namespace PhotoEditor
{
    delegate void RecognitionHandler(Boolean arg); // delegate type, for an event.

    runtimeclass Photo : Windows.UI.Xaml.Data.INotifyPropertyChanged // interface.
    {
        Photo(); // constructors.
        Photo(Windows.Storage.StorageFile imageFile);

        String ImageName{ get; }; // read-only property.
        Single SepiaIntensity; // read-write property.

        Windows.Foundation.IAsyncAction StartRecognitionAsync(); // (asynchronous) method.

        event RecognitionHandler ImageRecognized; // event.
    }
}
```

Note that the syntax of MIDL 3.0 is specifically and solely designed for *defining* types. You'll use a different programming language to *implement* those types. To use MIDL 3.0, you'll need Windows SDK version 10.0.17134.0 (Windows 10, version 1803) (`midl.exe` version 8.01.0622 or later, used with the `/winrt` switch).

## MIDL 1.0, 2.0, and 3.0
Interface Definition Language (IDL) began with the Distributed Computing Environment/Remote Procedure Calls (DCE/RPC) system. The original [MIDL 1.0](https://msdn.microsoft.com/library/windows/desktop/aa367091) is DCE/RPC IDL with enhancements for defining COM interfaces and coclasses.

An updated MIDL 2.0 syntax (also known as MIDLRT) was then developed within Microsoft to declare Windows Runtime APIs for the Windows platform. If you look in the Windows SDK folder `%WindowsSdkDir%Include<WindowsTargetPlatformVersion>\winrt` then you'll see examples of `.idl` files that are written with the MIDL 2.0 syntax. These are first-party Windows Runtime APIs, declared in their application binary interface (ABI) form. These files exist primarily for tooling to use&mdash;you won't author nor consume these APIs in this form (unless you're writing very low-level code).

Also see [Transition to MIDL 3.0 from classic MIDLRT](from-midlrt.md).

MIDL 3.0 is a much simpler and more modern syntax, whose purpose is to declare Windows Runtime APIs. And you can use it in your projects, particularly to define [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/index) runtime classes. The headers, for use from C++/WinRT, for the first-party Windows Runtime APIs are part of the SDK, inside the folder `%WindowsSdkDir%Include<WindowsTargetPlatformVersion>\cppwinrt\winrt`.

## Use cases for MIDL 3.0
In general, all Windows Runtime APIs are designed to be available to all Windows Runtime language projections. This is done, in part, by choosing to exclusively pass Windows Runtime types to and from Windows Runtime APIs. While it is a valid design decision to pass a raw COM interface to and from a Windows Runtime API, doing so limits the consumers of that particular Windows Runtime API to C++ applications. The technique can be seen in interoperation scenarios&mdash;for example, when interoperating between Direct3D and XAML. Since Direct3D is in the picture, the scenario is necessarily narrowed to C++ applications. So, an API that requires a COM interface doesn't impose any additional limitation over and above what's inherent. For example, a C++ application can obtain an [IDXGISwapChain](/windows/desktop/api/dxgi/nn-dxgi-idxgiswapchain) interface pointer, and then pass that to the [ISwapChainPanelNative::SetSwapChain method](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nf-windows-ui-xaml-media-dxinterop-iswapchainpanelnative-setswapchain). A C# application, for example, wouldn't be able to obtain an **IDXGISwapChain** to begin with, so it wouldn't be able to use that method for that reason. These interop-related exceptions live in interop headers, such as `windows.ui.xaml.media.dxinterop.h`.

If there *are* features or functionality of a COM component that you wish to expose to Windows Runtime language projections beyond C++, then you can create a C++ [Windows Runtime component](/windows/uwp/winrt-components/) (WRC) that directly creates and uses the COM component (such as DirectX, for example), and exposes a replication of some subset of its features and functionality in the form of a Windows Runtime API surface that takes and returns Windows Runtime types only. You could then consume that WRC from an application written in *any* Windows Runtime language projection.

## Definition structure, and calling midl.exe from the command line
The key organizational concepts in a MIDL 3.0 definition are namespaces, types, and members. A MIDL 3.0 source file (an `.idl` file) contains at least one namespace, inside which are types and/or subordinate namespaces. Each type contains zero or more members.

- Classes, interfaces, structures, and enumerations are types.
- Fields, methods, properties, and events are examples of members.

When you compile a MIDL 3.0 source file, the compiler (`midl.exe`) emits a Windows Runtime metadata file (typically a `.winmd` file).

```idl
// Bookstore.idl
namespace Bookstore
{
    runtimeclass BookSku : Windows.UI.Xaml.Data.INotifyPropertyChanged
    {
        BookSku();
        BookSku(Single price, String authorName, String coverImagePath, String title);

        Single Price;

        String AuthorName{ get; };
        Windows.UI.Xaml.Media.ImageSource CoverImage{ get; };
        String CoverImagePath{ get; };
        String Title{ get; };

        Boolean Equals(BookSku other);
        void ApplyDiscount(Single percentOff);
    }
}
```

Since the namespace of a Windows Runtime type becomes part of the type name, the example above defines a runtime class named **Bookstore.BookSku**. There's no language-independent way of expressing **BookSku** without also expressing the namespace.

This class implements the **Windows.UI.Xaml.Data.INotifyPropertyChanged** interface. And the class contains several members: two constructors, a read-write property (**Price**), some read-only properties (**AuthorName** through **Title**), and two methods, named **Equals** and **ApplyDiscount**. Note the use of the type **Single** rather than **float**. And that **String** has an upper-case "S".

> [!TIP]
> Visual Studio provides the best experience for compiling MIDL 3.0, by means of the C++/WinRT Visual Studio Extension (VSIX). See [Visual Studio support for C++/WinRT, and the VSIX](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt#visual-studio-support-for-cwinrt-xaml-the-vsix-extension-and-the-nuget-package).

But you can also compile MIDL 3.0 from the command line. If the source code for this example is stored in a file named `Bookstore.idl`, then you can issue the command below. If necessary for your case, you can update the SDK version number used in the command (which is 10.0.17134.0).

```console
midl /winrt /metadata_dir "%WindowsSdkDir%References\10.0.17134.0\windows.foundation.foundationcontract\3.0.0.0" /h "nul" /nomidl /reference "%WindowsSdkDir%References\10.0.17134.0\Windows.Foundation.FoundationContract\3.0.0.0\Windows.Foundation.FoundationContract.winmd" /reference "%WindowsSdkDir%References\10.0.17134.0\Windows.Foundation.UniversalApiContract\6.0.0.0\Windows.Foundation.UniversalApiContract.winmd" /reference "%WindowsSdkDir%\References\10.0.17134.0\Windows.Networking.Connectivity.WwanContract\2.0.0.0\Windows.Networking.Connectivity.WwanContract.winmd" Bookstore.idl
```

The `midl.exe` tool compiles the example and produces a metadata file named `Bookstore.winmd` (by default, the name of the `.idl` file is used). 

> [!TIP]
> If you use more than one IDL file (for advice about that, see [Factoring runtime classes into Midl files (.idl)](/windows/uwp/cpp-and-winrt-apis/author-apis#factoring-runtime-classes-into-midl-files-idl)), then merge all of the resulting `.winmd` files into a single file with the same name as the root namespace. That final `.winmd` file will be the one that the consumers of your APIs will reference.

In this case, **BookSku** is the only runtime class in the **Bookstore** namespace, so we saved a step and just named the `.idl` file for the namespace.

Incidentally, you can use the `where` command to find out where `midl.exe` is installed.

```console
where midl
```

If you want to use the types defined in one `.idl` file from a different `.idl` file, then you use the `import` directive. For more details, and a code example, see [XAML controls; bind to a C++/WinRT property](/windows/uwp/cpp-and-winrt-apis/binding-property). Of course, if you're consuming a first- or third-party component, then you won't have access to the `.idl` file. For example, you might want to consume the [Win2D](https://www.nuget.org/packages/Win2D.uwp) Windows Runtime API for immediate-mode 2D graphics rendering. The command above used the `/reference` switch to reference a Windows Runtime metadata (`.winmd`) file. In this next example, we'll use that switch again, imagining the scenario where we have `Bookstore.winmd`, but not `Bookstore.idl`.

```idl
// MVVMApp.idl
namespace MVVMApp
{
    runtimeclass ViewModel
    {
        ViewModel();
        Bookstore.BookSku BookSku{ get; };
    }
}
```

If the source code for the example above is stored in a file named `MVVMApp.idl`, then you can issue the command below to reference `Bookstore.winmd`.

```console
midl /winrt /metadata_dir "%WindowsSdkDir%References\10.0.17134.0\windows.foundation.foundationcontract\3.0.0.0" /h "nul" /nomidl /reference "%WindowsSdkDir%References\10.0.17134.0\Windows.Foundation.FoundationContract\3.0.0.0\Windows.Foundation.FoundationContract.winmd" /reference "%WindowsSdkDir%References\10.0.17134.0\Windows.Foundation.UniversalApiContract\6.0.0.0\Windows.Foundation.UniversalApiContract.winmd" /reference "%WindowsSdkDir%\References\10.0.17134.0\Windows.Networking.Connectivity.WwanContract\2.0.0.0\Windows.Networking.Connectivity.WwanContract.winmd" /reference Bookstore.winmd MVVMApp.idl
```

## Namespaces
A namespace is required. It prefixes the name of all types defined in the scope of the namespace block with the namespace name. A namespace can also contain subordinate namespace declarations. The name of types defined in a subordinate namespace scope have a prefix of all the containing namespace names.

The examples below are two ways of declaring the same **Windows.Foundation.Uri** class (as you can see, periods separate the levels of nested namespaces).

```idl
namespace Windows.Foundation
{
    runtimeclass Uri : IStringable
    {
        ...
    }
}
```

```idl
namespace Windows
{
    namespace Foundation
    {
        runtimeclass Uri : IStringable
        {
            ...
        }
    }
}
```

Here's another example showing that it's legal to declare namespaces and their types in a nested fashion.

```idl
namespace RootNs.SubNs1
{
    runtimeclass MySubNs1Class
    {
        void DoWork();
    }

    namespace SubNs2
    {
        runtimeclass MySubNs2Class
        {
            void DoWork();
        }
    }
}
```

But it's more common practice to close the previous namespace, and open a new one, like this.

```idl
namespace RootNs.SubNs1
{
    runtimeclass MySubNs1Class
    {
        void DoWork();
    }
}

namespace RootNs.SubNs1.SubNs2
{
    runtimeclass MySubNs2Class
    {
        void DoWork();
    }
}
```

## Types
There are two kinds of data types in MIDL 3.0: value types, and reference types. A variable of a value type directly contains its data. A variable of a reference type stores a reference to its data (such a variable is also known as an *object*).

It's possible for two reference type variables to reference the same object. Thus, an operation on one variable affects the object referenced by the other variable. With value types, the variables each have their own copy of the data, and it's not possible for an operation on one to affect the other (except in the case of `ref` and `out` parameter variables).

MIDL 3.0's value types are further divided into simple types, enum types, struct types, and nullable types.

MIDL 3.0's reference types are further divided into class types, interface types, and delegate types.

Here's an overview of MIDL 3.0's type system. Unlike previous versions of MIDL, you can't use aliases for these types.

<div class="mx-responsive-img">
<table class="uwpd-top-aligned-table">
  <tr class="header">
    <th colspan="2" align="left">Category</th>
    <th align="left">Description</th>
  </tr>
  <tr>
    <td rowspan="10">Value types</td>
    <td rowspan="7">Simple types</td>
    <td>Signed integral: <b>Int16</b>, <b>Int32</b>, <b>Int64</b></td>
  </tr>
  <tr>
    <td>Unsigned integral: <b>UInt8</b>, <b>UInt16</b>, <b>UInt32</b>, <b>UInt64</b></td>
  </tr>
  <tr>
    <td>Unicode characters: <b>Char</b> (represents a UTF-16LE; a 16-bit Unicode code unit)</td>
  </tr>
  <tr>
    <td>Unicode strings: <b>String</b></td>
  </tr>
  <tr>
    <td>IEEE floating point: <b>Single</b>, <b>Double</b></td>
  </tr>
  <tr>
    <td>Boolean: <b>Boolean</b></td>
  </tr>
  <tr>
    <td>128 bit UUID: <b>Guid</b></td>
  </tr>
  <tr>
    <td>Enum types</td>
    <td>User-defined types of the form <b>enum E {...}</b></td>
  </tr>
  <tr>
    <td>Struct types</td>
    <td>User-defined types of the form <b>struct S {...}</b></td>
  </tr>
  <tr>
    <td>Nullable types</td>
    <td>Extensions of all other value types with a <b>null</b> value</td>
  </tr>
  <tr>
    <td rowspan="4">Reference types</td>
    <td rowspan="2">Class types</td>
    <td>Ultimate base class of all other types: <b>Object</b></td>
  </tr>
  <tr>
    <td>User-defined types of the form <b>runtimeclass C {...}</b></td>
  </tr>
  <tr>
    <td>Interface types</td>
    <td>User-defined types of the form <b>interface I {...}</b></td>
  </tr>
  <tr>
    <td>Delegate types</td>
    <td>User-defined types of the form <b>delegate &lt;returnType&gt; D(...)</b></td>
  </tr>
</table>
</div>

The seven integral types provide support for 8-bit unsigned data; and 16-bit, 32-bit, and 64-bit values in signed or unsigned form.

The two floating point types, **Single** and **Double**, represent data using the 32-bit single-precision and 64-bit Double-precision IEEE 754 formats, respectively.

MIDL 3.0's **Boolean** type represents boolean values; either `true` or `false`.

Characters and strings in MIDL 3.0 contain Unicode characters. The **Char** type represents a UTF-16LE code unit; and the **String** type represents a sequence of UTF-16LE code units.

The following table summarizes MIDL 3.0's numeric types.

<div class="mx-responsive-img">
<table class="uwpd-top-aligned-table">
  <tr class="header">
    <th align="left">Category</th>
    <th align="left">Bits</th>
    <th align="left">Type</th>
    <th align="left">Range/Precision</th>
  </tr>
  <tr>
    <td rowspan="3">Signed integral</td>
    <td>16</td>
    <td><b>Int16</b></td>
    <td>–32,768...32,767</td>
  </tr>
  <tr>
    <td>32</td>
    <td><b>Int32</b></td>
    <td>–2,147,483,648...2,147,483,647</td>
  </tr>
  <tr>
    <td>64</td>
    <td><b>Int64</b></td>
    <td>–9,223,372,036,854,775,808...9,223,372,036,854,775,807</td>
  </tr>
  <tr>
    <td rowspan="4">Unsigned integral</td>
    <td>8</td>
    <td><b>UInt8</b></td>
    <td>0...255</td>
  </tr>
  <tr>
    <td>16</td>
    <td><b>UInt16</b></td>
    <td>0...65,535</td>
  </tr>
  <tr>
    <td>32</td>
    <td><b>UInt32</b></td>
    <td>0...4,294,967,295</td>
  </tr>
  <tr>
    <td>64</td>
    <td><b>UInt64</b></td>
    <td>0...18,446,744,073,709,551,615</td>
  </tr>
  <tr>
    <td rowspan="2">Floating point</td>
    <td>32</td>
    <td><b>Single</b></td>
    <td>1.5 × 10<sup>−45</sup> to 3.4 × 10<sup>38</sup>, 7-digit precision</td>
  </tr>
  <tr>
    <td>64</td>
    <td><b>Double</b></td>
    <td>5.0 × 10<sup>−324</sup> to 1.7 × 10<sup>308</sup>, 15-digit precision</td>
  </tr>
</table>
</div>

MIDL 3.0 source files use type definitions to create new types. A type definition specifies the name and the members of the new type. These MIDL 3.0 type categories are user-definable.

- attribute types,
- struct types,
- interface types,
- runtimeclass types,
- delegate types, and
- enum types.

An *attribute* type defines a Windows Runtime attribute that can be applied to other type definitions. An attribute provides metadata about the type to which the attribute is applied.

A *struct* type defines a Windows Runtime structure that contains data members. Structs are value types, and they do not require heap allocation. A data member of a struct type must either be a value type or a nullable type. Struct types do not support inheritance.

An *interface* type defines a Windows Runtime interface, which is a named set of function members. An interface may specify that an implementation of the interface must also implement of one or more specified additional (required) interfaces. Every interface type directly derives from the Windows Runtime [**IInspectable**](https://msdn.microsoft.com/en-us/library/br205821) interface.

A *runtimeclass* type defines a Windows Runtime class (runtime class). A runtime class contains members that can be properties, methods, and events.

A *delegate* type defines a Windows Runtime delegate, which represents a reference to a method with a particular parameter list and return type. Delegates make it possible to treat a method as an entity that can be passed as a parameter. A delegate is similar to the concept of a function pointer found in some other languages. Unlike function pointers, delegates are object-oriented, and type-safe.

An *enum* type is a distinct type with named constants. Every enum type has an implicit underlying type; either **Int32** or **UInt32**. The set of values of an enum type is the same as the set of values of the underlying type.

MIDL 3.0 supports three additional type categories.

- single-dimensional array types,
- nullable value types, and
- the **Object** type.

You don't need to declare a single-dimensional array before you can use it. Instead, array types are constructed by following a type name with square brackets. For example, **Int32[]** is a single-dimensional array of **Int32**.

Similarly, *nullable* value types also do not have to be defined before they can be used. For each non-nullable value type **T** (except **String**), there's a corresponding nullable type **Windows.Foundation.IReference&lt;T&gt;**, which can hold the additional value `null`. For instance, **Windows.Foundation.IReference&lt;Int32&gt;** is a type that can hold any 32-bit integer, or the value `null`. Also see [**IReference&lt;T&gt;**](/uwp/api/windows.foundation.ireference_t_).

Finally, MIDL 3.0 supports the **Object** type, which maps to the Windows Runtime [**IInspectable**](https://msdn.microsoft.com/en-us/library/br205821) interface. The *interface* and *runtimeclass* reference types conceptually derive from the **Object** type; *delegate* does not.

### Expressions in an enumerated value
With MIDL 3.0, you can only use an *expression* in the definition of the value of an enumerated type's named constants; in other words, in an enumeration initializer.

An expression is constructed from *operands* and *operators*. The operators in an expression indicate which operations to apply to the operands. Examples of operators include +, -, *, /, and `new`. Examples of operands include literals, fields, local variables, and expressions.

When an expression contains multiple operators, the *precedence* of the operators controls the order in which the individual operators are evaluated. For example, the expression x + y * z is evaluated as x + (y * z) because the * operator has higher precedence than the + operator.

The following table summarizes MIDL 3.0's operators, listing the operator categories in order of precedence from highest to lowest. Operators in the same category have equal precedence.

<div class="mx-responsive-img">
<table class="uwpd-top-aligned-table">
  <tr class="header">
    <th align="left">Category</th>
    <th align="left">Expression</th>
    <th align="left">Description</th>
  </tr>
  <tr>
    <td rowspan="2">Primary</td>
    <td>x++</td>
    <td>Post-increment</td>
  </tr>
  <tr>
    <td>x--</td>
    <td>Post-decrement</td>
  </tr>
  <tr>
    <td rowspan="6">Unary</td>
    <td>+x</td>
    <td>Identity</td>
  </tr>
  <tr>
    <td>-x</td>
    <td>Negation</td>
  </tr>
  <tr>
    <td>!x</td>
    <td>Logical negation</td>
  </tr>
  <tr>
    <td>~x</td>
    <td>Bitwise negation</td>
  </tr>
  <tr>
    <td>++x</td>
    <td>Pre-increment</td>
  </tr>
  <tr>
    <td>--x</td>
    <td>Pre-decrement</td>
  </tr>
  <tr>
    <td rowspan="3">Multiplicative</td>
    <td>x * y</td>
    <td>Multiplication</td>
  </tr>
  <tr>
    <td>x / y</td>
    <td>Division</td>
  </tr>
  <tr>
    <td>x % y</td>
    <td>Remainder</td>
  </tr>
  <tr>
    <td rowspan="2">Additive</td>
    <td>x + y</td>
    <td>Addition, String concatenation, delegate combination</td>
  </tr>
  <tr>
    <td>x – y</td>
    <td>Subtraction, delegate removal</td>
  </tr>
  <tr>
    <td rowspan="2">Shift</td>
    <td>x << y</td>
    <td>Shift left</td>
  </tr>
  <tr>
    <td>x >> y</td>
    <td>Shift right</td>
  </tr>
  <tr>
    <td>Logical AND</td>
    <td>x & y</td>
    <td>Integer bitwise AND, boolean logical AND</td>
  </tr>
  <tr>
    <td>Logical XOR</td>
    <td>x ^ y</td>
    <td>Integer bitwise XOR, boolean logical XOR</td>
  </tr>
  <tr>
    <td>Logical OR</td>
    <td>x | y</td>
    <td>Integer bitwise OR, boolean logical OR</td>
  </tr>
</table>
</div>

## Classes

*Classes* (or runtime classes) are the most fundamental of MIDL 3.0's types. A class is a definition of an aggregation of methods, properties, and events in a single unit. Classes support *inheritance* and *polymorphism*&mdash;mechanisms whereby *derived classes* can extend and specialize *base classes*.

You define a new class type using a class definition. A class
definition starts with a header that specifies the `runtimeclass`
keyword, the name of the class, the base class (if given), and the
interfaces implemented by the class. The header is followed by the class
body, which consists of a list of member declarations written between
the delimiters { and }.

Here's a definition of a simple class named **Area**.

```idl
runtimeclass Area
{
    Area(Int32 width, Int32 height);

    Int32 Height;
    Int32 Width;

    static Int32 NumberOfAreas { get; };
}
```

This defines a new Windows Runtime class named **Area**,
which has a constructor that take two **Int32** parameters, two **Int32**
read-write properties named **Height** and **Width**, and a static read-only
property named **NumberOfAreas**.

By default, a runtimeclass is sealed, and derivation from it is disallowed. See [Base classes](#base-classes).

In order to bind XAML to a view model, the view model runtime class needs to be defined in MIDL. See [XAML controls; bind to a C++/WinRT property](/windows/uwp/cpp-and-winrt-apis/binding-property) for more details.

You can declare that a class contains only static members, and supports no instances, by prefixing the runtime class definition with the `static` keyword. Adding a non-static member to the class then causes a compilation error.

```idl
static runtimeclass Area
{
    static Int32 NumberOfAreas { get; };
}
```

A static class is different from an empty class. Also see [Empty classes](advanced.md#empty-classes).

You can indicate that a class definition is incomplete by prefixing the runtime class definition with the `partial` keyword. All of the partial class definitions encountered by the compiler are combined into a single runtime class. This feature is primarily for XAML authoring scenarios, where some of the partial classes are machine-generated.

|Modifier|Meaning|
|-|-|
|static|Class contains only static members|
|partial|Class definition is incomplete|

See [Composition and activation](advanced.md#composition-and-activation) for advanced modifiers.

### Member access modifiers
As MIDL 3.0 is a definition language for describing the public surface
of Windows Runtime types, there's no need for explicit syntax to
declare the public accessibility of a member. All members are implicitly
public. That's why MIDL 3.0 doesn't require nor allow the (effectively
redundant) `public` keyword.

### Base classes
A class definition may specify a base class by following the class name and type parameters with a colon and the name of the base class. Omitting a base class specification is the same as deriving from type **Object** (in other words, from [**IInspectable**](https://msdn.microsoft.com/en-us/library/br205821)).

> [!NOTE]
> Your view model classes&mdash;in fact, any runtime class that you define in your application&mdash;need not derive from a base class.
>
> Any runtime class that you define in the application that *does* derive from a base class is known as a *composable* class. And there are constraints around composable classes. For an application to pass the [Windows App Certification Kit](/windows/uwp/debug-test-perf/windows-app-certification-kit) tests used by Visual Studio and by the Microsoft Store to validate submissions (and therefore for the application to be successfully ingested into the Microsoft Store), a composable class must ultimately derive from a Windows base class. Meaning that the class at the very root of the inheritance hierarchy must be a type originating in a Windows.* namespace.
>
> See [XAML controls; bind to a C++/WinRT property](/windows/uwp/cpp-and-winrt-apis/binding-property) for more details.

In the next example, the base class of **Volume** is **Area**, and the base class of **Area** is **Windows.UI.Xaml.DependencyObject**.

```idl
unsealed runtimeclass Area : Windows.UI.Xaml.DependencyObject
{
    Area(Int32 width, Int32 height);
    Int32 Height;
    Int32 Width;
}

runtimeclass Volume : Area
{
    Volume(Int32 width, Int32 height, Int32 depth);
    Int32 Depth;
}
```

> [!NOTE]
> Here, **Area** and **Volume** are defined in the same source file. For a discussion of the pros and cons, see [Factoring runtime classes into Midl files (.idl)](/windows/uwp/cpp-and-winrt-apis/author-apis#factoring-runtime-classes-into-midl-files-idl).

A class inherits the members of its base class. Inheritance means that a
class implicitly contains all members of its base class, except for the
constructor(s) of the base class. A derived class can add new members to
those it inherits, but it cannot remove the definition of an inherited
member.

In the previous example, **Volume** inherits the **Height** and **Width** properties
from **Area**. So, every **Volume** instance contains three properties:
**Height**, **Width**, and **Depth**.

In general, type resolution rules require that a type name is fully qualified when referenced. An exception is when the type has been defined in the same namespace as the current type. The example above works as written if **Area** and **Volume** are both in the same namespace.

### Implemented interfaces
A class definition may also specify a list of interfaces that the class
implements. You specify the interfaces as a comma-separated list of
interfaces following the (optional) base class.

In the example below, the **Area** class implements the [**IStringable**](/uwp/api/windows.foundation.istringable) interface; and the **Volume** class implements both **IStringable** and the hypothetical **IEquatable** interface.

```idl
unsealed runtimeclass Area : Windows.Foundation.IStringable
{
    Area(Int32 width, Int32 height);
    Int32 Height;
    Int32 Width;
}

runtimeclass Volume : Area, Windows.Foundation.IStringable, IEquatable
{
    Volume(Int32 width, Int32 height, Int32 depth);
    Int32 Depth;
}
```

In the MIDL, you don't declare the interface's members on the class. You do, of course, have to declare and define them on the actual implementation.

### Members
The members of a class are either *static members* or *instance
members*. A static member belongs to a class. An instance member
belongs to an object (that is, an instance of a class).

This table shows the kinds of member that a class can contain.

|Member kind|Description|
|-|-|
|Constructors|Actions required to initialize an instance of the class, or to initialize the class itself|
|Properties|Actions associated with reading and writing named properties of an instance of the class, or of the class itself|
|Methods|Computations and actions that can be performed by an instance of the class, or by the class itself|
|Events|Notifications that can be raised by an instance of the class|

#### Constructors
MIDL 3.0 supports the declaration of instance constructors. An *instance
constructor* is a method that implements the actions required to
initialize an instance of a class. Constructors may not be static.

A constructor is declared like an instance method (but with no return
type), and with the same name as the containing class.

Instance constructors can be overloaded. For example, the **Test** class below declares three instance constructors; one with no parameters (the *default* constructor), one that takes an **Int32** parameter, and one that takes two **Double** parameters (*parameterized* constructors).

```idl
runtimeclass Test
{
    Test();
    Test(Int32 x);
    Test(Double x, Double y);
}
```

For details on the syntax for parameter lists, see [Methods](#methods) below.

Instance properties, methods, and events are inherited. Instance constructors are not inherited (with one exception), and a class has no instance constructors other than those
actually declared in the class. If no instance constructor is supplied
for a class, then you cannot directly instantiate the class. For such a class, you'd typically have a factory method elsewhere that returns an instance of the class.

The exception is unsealed classes. An unsealed class can have one or more protected constructors.

#### Properties
*Properties* are conceptually similar to fields. Both are a member with a name and an associated type. However, unlike fields, properties do not
denote storage locations. Instead, properties have *accessors* that
specify the function to be executed when you read or write a property.

A property is declared like a field, except that the declaration ends
with a `get` keyword and/or a `set` keyword written between the delimiters {
and }, and ending in a semicolon.

A property that has both a `get` keyword and a `set` keyword is a
*read-write property*. A property that has only a `get` keyword is a
*read-only property*. And a property that has only a `set` keyword is
a *write-only property*.

For example, the class **Area**, seen previously, contains two read-write properties named **Height** and **Width**.

```idl
unsealed runtimeclass Area
{
    Int32 Height { get; set; };
    Int32 Width; // get and set are implied if both are omitted.
}
```

The declaration of **Width** omits the braces
and the `get` and `set` keywords. The omission
implies that the property is read-write, and is semantically identical to
providing the `get` and `set` keywords in that order&mdash;`get`, followed by `set`.

Additionally, you can specify only the `get` keyword to indicate that the
property is read-only.

```idl
// Read-only instance property returning mutable collection.
Windows.Foundation.Collections.IVector<Windows.UI.Color> Colors { get; };
```

The Windows Runtime doesn't support write-only properties. But you can specify only the `set` keyword to revise an existing read-only property into a read-write property. Take this version of **Area** as an example.

```idl
unsealed runtimeclass Area
{
    ...
    Color SurfaceColor { get; };
}
```

If you want subsequently to make the **SurfaceColor** property read-write, and you don't need to maintain binary compatibility with prior definitions of **Area** (for example, the **Area** class is a type in an application that you
recompile each time), then you can simply add the `set` keyword to the existing
**SurfaceColor** declaration like this.

```idl
unsealed runtimeclass Area
{
    ...
    Color SurfaceColor { get; set; };
}
```

If, on the other hand, you *do* need binary stability (for example, the **Area** class is a component in a library that you ship to customers), then you cannot add the `set` keyword to the existing property declaration. Doing so changes the binary interface to your class.

In that case, add the property `set` keyword to an additional
definition of the property at the end of the class like this.

```idl
unsealed runtimeclass Area
{
    ...
    Color SurfaceColor { get; };
    ...
    Color SurfaceColor { set; };
}
```

The compiler produces an error for a write-only property. But that's not what's being done here. Because of the preceding declaration of the property
as read-only, the addition of the set keyword doesn't declare a
write-only property, but instead a read-write property.

The Windows Runtime implementation of a property is one or two accessor
methods on an interface. The order of the get and set keywords in the
property declaration determine the order of the get and set accessor
methods in the backing interface.

The `get` accessor corresponds to a parameterless method with a return
value of the property type&mdash;the property getter.

A `set` accessor corresponds to a method with a single parameter named
*value*, and no return type&mdash;the property setter.

Consequently, these two declarations produce different binary interfaces.

```idl
Color SurfaceColor { get; set; };
```

```idl
Color SurfaceColor { set; get; };
```

##### Static and instance properties
Similar to fields and methods, MIDL 3.0 supports both instance
properties and static properties. Static properties are declared with
the `static` modifier prefixed, and instance properties are declared without it.

#### Methods
A *method* is a member that implements a computation or action that
can be performed by an instance of the class, or by the class itself. A *static method* is accessed through the class. An *instance method* is accessed through an instance of the class.

A method has a (possibly empty) list of *parameters*, which
represent values or variable references passed to the method. A method also has a *return type*, which specifies the type of the value computed and
returned by the method. A method's return type is `void` if it doesn't
return a value.

```idl
// Instance method with no return value.
void AddData(String data);

// Instance method *with* a return value.
Int32 GetDataSize();

// Instance method accepting/returning a runtime class.
// Notice that you don't say "&" nor "*" for reference types.
BasicClass MergeWith(BasicClass other);

// Asynchronous instance methods.
Windows.Foundation.IAsyncAction UpdateAsync();
Windows.Foundation.IAsyncOperation<Boolean> TrySaveAsync();

// Instance method that returns a value through a parameter.
Boolean TryParseInt16(String input, out Int16 value);

// Instance method that receives a reference to a value type.
Double CalculateArea(ref const Windows.Foundation.Rect value);

// Instance method accepting or returning a conformant array.
void SetBytes(UInt8[] bytes);
UInt8[] GetBytes();

// instance method that writes to a caller-provided conformant array
void ReadBytes(ref UInt8[] bytes);
```

The *signature* of a method must be unique in the class in which the
method is declared. The signature of a method consists of the name of
the method, the types of its parameters, and/or the number of its
parameters. The signature of a method doesn't include the return type.

#### Method visibility modifiers
A *method* may have one of two optional visibility modifiers when the method is present in a derived class.

The *overridable* modifier states that this method overrides a
method with the same name and signature in a base class.

The *protected* modifier states that this method is only accessible
by members in a subsequently derived class.

##### Method overloading
Method *overloading* permits multiple methods in the same class to
have the same name as long as their parameters differ in number (in other words the methods have different *arity*).

```idl
runtimeclass Test
{
    static void F();
    static void F(Double x);
    static void F(Double x, Double y);
}
```

> [!NOTE]
> All methods with the same name must have differing *arity*. The Windows Runtime doesn't support overloading by the same arity but with differing parameter types.

##### Parameters
*Parameters* are used to pass values, or variable references, to a method. A *parameter* describes a range of allowable values, and a name. An *argument* is an actual value passed in practice where a parameter is expected.

So, parameters of a method get their actual values from the specific
*arguments* that are specified when the method is invoked. There are
four kinds of parameters: value parameters, const reference parameters,
output parameters, and array parameters.

A *value parameter* is used to pass an input parameter. A value
parameter gets its initial value from the argument that was passed for
the parameter. Modifications to a value parameter do not affect the
argument that was passed for the parameter. So, a value parameter
is effective a `const` input parameter.

A *const reference parameter* is used for efficient input parameter
passing of large value types. Methods receive such parameters as a
reference to the actual value, rather than receiving a copy of the
actual value. For large value types, it's more efficient to pass (to a function) a
pointer-sized reference to a value than to pass a copy of the actual
value itself.

A const reference parameter is declared with the `const ref` modifier. This example shows the use of `const ref` parameters; a practical choice when accepting a value as large as a [**Matrix4X4**](/uwp/api/windows.foundation.numerics.matrix4x4).

```idl
runtimeclass Test
{
    static void Swap(const ref Matrix4X4 x, const ref Matrix4X4 y);
}
```

An *output parameter* is used for output parameter passing. For an
output parameter, the callee receives a pointer to the location in which
the value is returned. An output parameter is declared with the `out`
modifier. The following example shows the use of `out` parameters.

```idl
runtimeclass Test
{
    static void Divide(Int32 x, Int32 y, out Int32 result, out Int32 remainder);
}
```

Note that JavaScript projects a method with multiple `out` parameters
differently than most languages do. JavaScript projects the preceding
method as returning a single object; and the returned object has two
properties. The properties have the names of the `out` parameters. In
the preceding example, the JavaScript object returned by the method call
has a property named *result*, and another property named
*remainder*.

An *array* is a data structure that contains a number of variables that are accessed through computed indices. The variables contained in
an array&mdash;also called the *elements* of the array&mdash;are all of the
same type, and this type is called the *element type* of the array.

An *array parameter* is a reference type, and the declaration
allocates space for a reference to an array instance.

```idl
runtimeclass Test
{
    void PassArray (Int32[] values);
    void FillArray (ref Int32[] values);
    void ReceiveArray (out Int32[] values);
}
```

MIDL 3.0 supports declarations of a *single-dimensional array*.

##### Static and instance methods
A method declared with a `static` modifier prefixed is a *static method*. A
static method has no access to a specific instance, and therefore can
only directly access other static members of the class.

A method declared without a `static` modifier is an *instance method*.
An instance method has access to a specific instance, and can access both
static and instance members of the class.

The following **Entity** class has both static and instance members.

```idl
runtimeclass Entity
{
    Int32 SerialNo { get; };
    static Int32 GetNextSerialNo();
    static void SetNextSerialNo(Int32 value);
}
```

Each **Entity** instance contains its own serial number (and presumably some
other information that is not shown here). Internally, the **Entity** constructor (which is like an instance method) initializes the new instance with the next
available serial number.

The **SerialNo** property provides access to the serial number for the
instance on which you invoke the *property get* method.

The **GetNextSerialNo** and **SetNextSerialNo** static methods can access the internal *next available serial number* static member of the **Entity** class.

##### Protected and override methods
All methods in a Windows Runtime type are effectively virtual. When a
virtual method is invoked, the *run-time type* of the instance for
which that invocation takes place determines the actual method
implementation to invoke.

A method can be *overridden* in a derived class. When an instance
method declaration includes an `override` modifier, the method overrides
an inherited virtual method with the same signature. Whereas a method
declaration ordinarily *introduces* a new method, an `override` method declaration
*specializes* an existing inherited virtual method by providing a new
implementation of that method.

When an instance method declaration includes a `protected` modifier, the
method is only visible to derived classes.

#### Events
An *event* declaration is a member that specifies that a class is an
event source. Such an event source provides notifications to any recipient that implements a delegate (a method with a specific signature).

You declare an event using the `event` keyword, followed by the delegate type
name (which describes the required method signature), followed by the name
of the event. Here's an example event that uses an existing delegate type from the platform.

```idl
runtimeclass Area
{
    ...
    event Windows.UI.Xaml.WindowSizeChangedEventHandler SizeChanged;
    ...
}
```

An event declaration implicitly adds two methods to the class: an *add*
method, which a client calls to add an event handler to the source, and a
*remove* method, which a client calls to remove a previously added event
handler. Here are more example.

```idl
// Instance event with no payload.
event Windows.Foundation.TypedEventHandler<BasicClass, Object> Changed;

// Instance event with event parameters.
event Windows.Foundation.TypedEventHandler<BasicClass, BasicClassSaveCompletedEventArgs> SaveCompleted;

// Static event with no payload.
static event Windows.Foundation.EventHandler<Object> ResetOccurred;

// Static event with event parameters.
static event Windows.Foundation.EventHandler<BasicClassDeviceAddedEventArgs> DeviceAdded;
```

### Delegates
A *delegate type* specifies a method with a particular parameter list and return type. A single instance of an event can contain any number of references to instances of its delegate type. The declaration is similar to that of a regular member method, except that it exists outside of a runtime class, and it's prefixed with the `delegate` keyword.

A delegate makes it possible to treat methods as entities that can be assigned to variables and passed as parameters. Delegates are similar to the concept of function pointers found in some other languages. But, unlike function pointers, delegates are object-oriented and type-safe.

If we don't want to use the [**WindowSizeChangedEventHandler**](/uwp/api/windows.ui.xaml.windowsizechangedeventhandler) delegate type from the platform, then we can define our own delegate type.

```idl
delegate void SizeChangedHandler(Object sender, Windows.UI.Core.WindowSizeChangedEventArgs args);
```

An instance of our **SizeChangedHandler** delegate type can reference any method that takes two arguments (an **Object**, and a [**WindowSizeChangedEventArgs**](/uwp/api/windows.ui.core.windowsizechangedeventargs)), and returns void. After we've discussed *structs*, you'll also be able to replace the **WindowSizeChangedEventArgs** parameter with an *event args* type of your own.

An interesting and useful property of a delegate is that it doesn't know or care about the class of the method it references; all that matters is that the referenced method has the same parameters and return type as the delegate.

You can optionally attribute a delegate declaration with `[uuid(...)]`.

Also see [Delegates returning HRESULT](advanced.md#delegates-returning-hresult).

### Structs

A *struct* is a data structure that can contain data members. But, unlike a class, a struct is a value type.

Structs are particularly useful for small data structures that have
value semantics. Complex numbers, event args, points in a coordinate system, or
key-value pairs in a dictionary are all good examples of structs. The
use of structs rather than classes for small data structures can make a
large difference in the number of memory allocations that an application
performs.

Let's use an example to contrast classes and structs. Here's a version of **Point** first as a *class*.

```idl
runtimeclass Point
{
    Point(Int32 x, Int32 y);
    Int32 x;
    Int32 y;
}
```

This C# program creates and initializes an array of 100 instances of **Point**. With **Point** implemented as a class, 101 separate objects are
instantiated: one for the array object itself; and one for each of the 100 **Point** elements.

```csharp
class Test
{
    static Test()
    {
        Point[] points = new Point[100];
        for (Int32 i = 0; i < 100; ++i) points[i] = new Point(i, i);
    }
}
```

A more performant alternative is to make **Point** a struct, instead of a class.

```idl
struct Point
{
    Int32 x;
    Int32 y;
}
```

Now, only one object is instantiated&mdash;the array object itself. The **Point** elements are stored in line inside the array; a memory arrangement that processor caches are able to use to powerful effect.

Structs implemented as part of Windows itself are not altered once introduced.

### Interfaces
An *interface* defines a contract that can be implemented by
classes. An interface can contain methods, properties, and events&mdash;just
like classes.

Unlike a class, an interface doesn't provide implementations of the
members it defines. It merely specifies the members that must be supplied
by any class that implements the interface.

Interfaces may *require* a class that implements the interface to
also implement other interfaces. In the following example, the interface
**IComboBox** requires that any class implementing **IComboBox**, also implement
both **ITextBox** and **IListBox**. Additionally, a class implementing **IComboBox**
must also implement **IControl**. That's because both **ITextBox** and **IListBox** require *it*.

```idl
interface IControl
{
    void Paint();
}

interface ITextBox requires IControl
{
    void SetText(String text);
}

interface IListBox requires IControl
{
    void SetItems(String[] items);
}

interface IComboBox requires ITextBox, IListBox
{
    ...
}
```

A class can implement zero or more interfaces. In the next example,
the class **EditBox** implements both **IControl** and **IDataBound**.

```idl
interface IDataBound
{
    void Bind(Binder b);
}

runtimeclass EditBox : IControl, IDataBound
{
}
```

You should only define an interface if you expect developers who consume your types to implement it.

### Enums

An *enum type* (or enumerated type, or enumeration) is a distinct value type with a set of named
constants. The following example defines and uses an enum type named
**Color** with three constant values: **Red**, **Green**, and **Blue**.

```idl
enum Color
{
    Red,
    Green,
    Blue, // Trailing comma is optional, but recommended to make future changes easier.
};
```

Each enum type has a corresponding integral type called the *underlying type* of the enum type. The underlying type of an enum is either **Int32** or **UInt32**.

The Windows Runtime supports two kinds of enums: *normal* enums, and *flags* enums. An enum of the normal kind expresses a set of exclusive values; while one of the flags kind represents a set of Boolean values. To enable bitwise operators for a flags enum, the MIDL 3.0 compiler generates C++ operator overloads.

A flags enum has the `[flags]` attribute applied. In that case, the underlying type of the enum is **UInt32**. When the `[flags]` attribute is not present (a normal enum), the underlying type of the enum is **Int32**. It's not possible to declare an enum as any other type.

```idl
[flags]
enum SetOfBooleanValues
{
    None   = 0x00000000,
    Value1 = 0x00000001,
    Value2 = 0x00000002,
    Value3 = 0x00000004,
};
```

An enum type's storage format and range of possible values are determined by its underlying type. The set of values that an enum type can take on is not limited by its declared enum members.

The following example defines an enum type named **Alignment**, with an
underlying type of **Int32**.

```idl
enum Alignment
{
    Left = -1,
    Center = 0,
    Right = 1
};
```

As is also true for C and C++, a MIDL 3.0 enum can include a constant expression that
specifies the value of the member (as seen above). The constant value for each enum
member must be in the range of the underlying type of the enum. When an
enum member declaration doesn't explicitly specify a value, the member
is given the value zero (if it is the first member in the enum type), or
the value of the textually preceding enum member plus one.

The following example defines an enum type named **Permissions**, with an
underlying type of **UInt32**.

```idl
[flags]
enum Permissions
{
    None = 0x0000,
    Camera = 0x0001,
    Microphone = 0x0002
};
```

### Attributes
Types, members, and other entities in MIDL 3.0 source code support
modifiers that control certain aspects of their behavior. For example,
the accessibility of a method is controlled using the `protected`
access modifier. MIDL 3.0 generalizes this capability such that user-defined
types of declarative information can be attached to program entities, and
retrieved at run-time from the metadata.

Programs specify this additional declarative information by defining and
using *attributes*.

The next example defines a **HelpAttribute** attribute, which can be
placed on program entities to provide links to their associated
documentation.

```idl
[attributeusage(target_runtimeclass_member)]
attribute HelpAttribute
{
    HelpAttribute(String classUri);
    String ClassUri { get; };
    String MemberTopic { get; set; };
}
```

An attribute can be applied by giving its name, along with any
arguments, inside square brackets just before the associated
declaration. If an attribute's name ends in Attribute, then that part of the
name can be omitted when the attribute is referenced. For example, the
**HelpAttribute** attribute can be used like this.

```idl
[Help("https://docs.contoso.com/.../Widget")]
runtimeclass Widget
{
    [Help("https://docs.contoso.com/.../Widget", MemberTopic="Display")]
    void Display(String text);
}
```

You can apply the same attribute to multiple
declarations by using a scope block following the
attribute. That is, an attribute immediately followed by braces surrounding
the declarations to which the attribute applies.

```idl
runtimeclass Widget
{
    [Custom()]
    {
        void Display(String text);
        void Print();
        Single Rate;
    }
}
```

Attributes implemented as part of Windows itself are usually in the **Windows.Foundation** namespace.

As shown in the first example, you use the `[attributeusage(<target>)]` attribute on your attribute definition. Valid target values are `target_all`, `target_delegate`, `target_enum`, `target_event`, `target_field`, `target_interface`, `target_method`, `target_parameter`, `target_property`, `target_runtimeclass`, `target_runtimeclass_member`, and `target_struct`. You can include multiple targets within the parentheses, separated by commas.

Other attributes you can apply to an attribute are `[allowmultiple]` and `[attributename("<name>")]`.

## Parameterized types

The example below produces *error MIDL2025: [msg]syntax error [context]: expecting > or, near ">>"*.

```idl
Windows.Foundation.IAsyncOperation<Windows.Foundation.Collections.IVector<String>> RetrieveCollectionAsync();
```

Instead, insert a space between the two `>` characters so that the pair of template-closing characters is not misinterpreted as a right-shift operator.

```idl
Windows.Foundation.IAsyncOperation<Windows.Foundation.Collections.IVector<String> > RetrieveCollectionAsync();
```

The example below produces *error MIDL2025: [msg]syntax error [context]: expecting > or, near "["*. This is because it's invalid to use an array as a parameter type argument to a parameterized interface. But also see [**IReferenceArray\<T\>**](/uwp/api/windows.foundation.ireferencearray_t_).

```idl
Windows.Foundation.IAsyncOperation<Int32[]> RetrieveArrayAsync();
```

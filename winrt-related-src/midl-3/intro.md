---
author: stevewhims
description: An introduction to Microsoft Interface Definition Language 3.0.
title: Introduction to Microsoft Interface Definition Language 3.0
ms.author: stwhi
ms.date: 04/23/2018
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, winrt, api, reference, idl, midl, 3.0
ms.localizationpriority: medium
---

# Introduction to Microsoft Interface Definition Language 3.0
> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

Microsoft Interface Definition Language (MIDL) 3.0 is a simplified, modern syntax for declaring Windows Runtime types inside Interface Definition Language (`.idl`) files. This new syntax will feel familiar to anyone experienced with C, C++, C#, and/or Java. MIDL 3.0 is a particularly convenient way to declare [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/index) runtime classes. Here's how it looks.

```idl
// booksku.idl
import "Windows.Foundation.idl";
namespace Bookstore
{
    runtimeclass BookSku
    {
        String Title;
    }
}
```

Note that the syntax of MIDL 3.0 is specifically and solely designed for *declaring* types. You'll use a different programming language to *implement* those types. To use MIDL 3.0, you'll need Windows SDK version 10.0.17134.0 (Windows 10, version 1803) (`midl.exe` version 8.01.0622 or later, used with the `/winrt` switch).

## Declaration structure
The key organizational concepts in a MIDL 3.0 declaration are namespaces, types, and members. A MIDL 3.0 source file (an `.idl` file) contains at least one namespace, inside which are types and/or subordinate namespaces. Each type contains zero or more members.

- Classes, interfaces, structures, and enumerations are types.
- Fields, methods, properties, and events are examples of members.

When you compile a MIDL 3.0 source file, the compiler (`midl.exe`) emits a Windows Runtime metadata file (typically a `.winmd` file), and a header for use by C and C++ applications.

```idl
// booksku.idl
import "Windows.UI.Xaml.Data.idl";
import "Windows.UI.Xaml.Media.idl";
namespace Bookstore
{
    runtimeclass BookSku : Windows.UI.Xaml.DependencyObject, Windows.UI.Xaml.Data.INotifyPropertyChanged
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

Since the namespace of a Windows Runtime type becomes part of the type name, the example above declares a runtime class named **Bookstore.BookSku**. There's no language-independent way of expressing **BookSku** without also expressing the namespace.

This class implements the **Windows.UI.Xaml.Data.INotifyPropertyChanged** interface. And the class contains several members: two constructors, a read-write property (**Price**), some read-only properties (**AuthorName** through **Title**), and two methods, named **Equals** and **ApplyDiscount**. Note the use of the type **Single** rather than **float**. And that **String** has an upper-case "S".

If the source code for this example is stored in `booksku.idl`, then you can issue this command (adjust the SDK version number for your case, if necessary).

```
midl /winrt /metadata_dir "%WindowsSdkDir%References\10.0.17133.0\windows.foundation.foundationcontract\3.0.0.0" /nomidl booksku.idl
```

The `midl.exe` tool compiles the example and produces a metadata file named `booksku.winmd`, and a header named `booksku.h`. Incidentally, you can use the `where` command to find out where `midl.exe` is installed.

```
where midl
```

## Namespaces
A namespace is required. It prefixes the name of all types defined in the scope of the namespace block with the namespace name. A namespace can also contain subordinate namespace declarations. The name of types declared in a subordinate namespace scope have a prefix of all the containing namespace names.

The examples below are two ways of declaring the same **Windows.Foundation.Uri** class.

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

## Types
There are two kinds of data types in MIDL 3.0: value types, and reference types. A variable of a value type directly contains its data. A variable of a reference type stores a reference to its data (such a variable is also known as an *object*).

It's possible for two reference type variables to reference the same object. Thus, an operation on one variable affects the object referenced by the other variable. With value types, the variables each have their own copy of the data, and it's not possible for an operation on one to affect the other (except in the case of `ref` and `out` parameter variables).

MIDL 3.0's value types are further divided into simple types, enum types, struct types, and nullable types.

MIDL 3.0's reference types are further divided into class types, interface types, and delegate types.

Here's an overview of MIDL 3.0's type system.

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
    <td>Unicode characters: <b>Char</b></td>
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

MIDL 3.0 source files use type declarations to create new types. A type declaration specifies the name and the members of the new type. These MIDL 3.0 type categories are user-definable.

- attribute types,
- struct types,
- interface types,
- runtimeclass types,
- delegate types, and
- enum types.

An *attribute* type declares a Windows Runtime attribute that can be applied to other type declarations. An attribute provides metadata about the type to which the attribute is applied.

A *struct* type declares a Windows Runtime structure that contains data members. Structs are value types, and they do not require heap allocation. A data member of a struct type must either be a value type or a nullable type. Struct types do not support inheritance.

An *interface* type declares a Windows Runtime interface, which is a named set of function members. An interface may specify that an implementation of the interface must also implement of one or more specified additional (required) interfaces. Every interface type directly derives from the Windows Runtime [**IInspectable**](https://msdn.microsoft.com/en-us/library/br205821) interface.

A *runtimeclass* type declares a Windows Runtime class (runtime class). A runtime class contains members that can be properties, methods, and events.

A *delegate* type declares a Windows Runtime delegate, which represents a reference to a method with a particular parameter list and return type. Delegates make it possible to treat a method as an entity that can be passed as a parameter. A delegate is similar to the concept of a function pointer found in some other languages. Unlike function pointers, delegates are object-oriented, and type-safe.

An *enum* type is a distinct type with named constants. Every enum type has an implicit underlying type; either **Int32** or **UInt32**. The set of values of an enum type is the same as the set of values of the underlying type.

MIDL 3.0 supports three additional type categories.

- single-dimensional array types,
- nullable value types, and
- the **Object** type.

You don't need to declare a single-dimensional array before you can use it. Instead, array types are constructed by following a type name with square brackets. For example, **Int32[]** is a single-dimensional array of **Int32**.

Similarly, *nullable* value types also do not have to be declared before they can be used. For each non-nullable value type **T** (except **String**), there's a corresponding nullable type **Windows.Foundation.IReference&lt;T&gt;**, which can hold the additional value `null`. For instance, **Windows.Foundation.IReference&lt;Int32&gt;** is a type that can hold any 32-bit integer, or the value `null`. Also see [**IReference&lt;T&gt;**](/uwp/api/windows.foundation.ireference_t_).

Finally, MIDL 3.0 supports the **Object** type, which maps to the Windows Runtime [**IInspectable**](https://msdn.microsoft.com/en-us/library/br205821) interface. The *interface* and *runtimeclass* reference types conceptually derive from the **Object** type; *delegate* does not.

### Expressions in an enumerated value
With MIDL 3.0, you can only use an *expression* in the declaration of the value of an enumerated type's named constants; in other words, in an enumeration initializer.

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
*Classes* are the most fundamental of MIDL 3.0's types. A class is a declaration of an aggregation of methods, properties, and events in a single unit. Classes support *inheritance* and *polymorphism*&mdash;mechanisms whereby *derived classes* can extend and specialize *base classes*.

You declare a new class type using a class declaration. A class
declaration starts with a header that specifies the `runtimeclass`
keyword, the name of the class, the base class (if given), and the
interfaces implemented by the class. The header is followed by the class
body, which consists of a list of member declarations written between
the delimiters { and }.

Here's a declaration of a simple class named **Area**.

```idl
unsealed runtimeclass Area
{
    Area(Int32 width, Int32 height);

    Int32 Height;
    Int32 Width;
    
  static Int32 NumberOfAreas { get; };
}
```

This declares a new unsealed Windows Runtime class named **Area**,
which has a constructor that take two **Int32** parameters, two **Int32**
read-write properties named **Height** and **Width**, and a static read-only
property named **NumberOfAreas**.

An *unsealed* class is a class that you can use as a base class. In other words, a subsequent class can derive from an unsealed class. By default, a runtimeclass is sealed and derivation from it is disallowed.

> [!IMPORTANT]
> For an application to pass [Windows App Certification Kit](/windows/uwp/debug-test-perf/windows-app-certification-kit) tests, and to be successfully ingested into the Microsoft Store, the ultimate base class of each runtime class *declared in the application* must be a type originating in a Windows.* namespace.

In order to bind XAML to a view model, the view model runtime class needs to be declared in MIDL. In a case like that, derive each view model from [**Windows.UI.Xaml.DependencyObject**](/uwp/api/windows.ui.xaml.dependencyobject). Alternatively, declare a bindable base class derived from **DependencyObject**, and derive your view models from that.

You can declare your data models as C++ structs; they don't need to be declared in MIDL (as long as you're consuming them only from your view models and not binding XAML directly to them; in which case they'd arguably be view models by definition, anyway).

### Member access modifiers
As MIDL 3.0 is a declaration language for describing the public surface
of Windows Runtime types, there's no need for explicit syntax to
declare the public accessibility of a member. All members are implicitly
public. That's why MIDL 3.0 doesn't require nor allow the (effectively
redundant) `public` keyword.

You can declare that a class contains only static members by prefixing
the runtime class declaration with the `static` keyword. Adding a
non-static member to the class then causes a compilation error.

```idl
static runtimeclass Area
{
    static Int32 NumberOfAreas { get; };
}
```

|Access modifier|Meaning|
|-|-|
|static|Class contains only static members|

### Base classes
A class declaration may specify a base class by following the class name
and type parameters with a colon and the name of the base class.
Omitting a base class specification is the same as deriving from type
**Object** (in other words, from [**IInspectable**](https://msdn.microsoft.com/en-us/library/br205821)).

> [!IMPORTANT]
> For an application to pass [Windows App Certification Kit](/windows/uwp/debug-test-perf/windows-app-certification-kit) tests, and to be successfully ingested into the Microsoft Store, the ultimate base class of each runtime class *declared in the application* must be a type originating in a Windows.* namespace; for example, [**Windows.UI.Xaml.DependencyObject**](/uwp/api/windows.ui.xaml.dependencyobject). For more info, see [XAML controls; binding to a C++/WinRT property](/windows/uwp/cpp-and-winrt-apis/binding-property#create-a-blank-app-bookstore).

In the next example, the base class of **Volume** is **Area**, and the (implicit) base class of **Area** is **Object**.

```idl
unsealed runtimeclass Area
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
> Here, **Area** and **Volume** are declared in the same source file, but we recommend that you declare each runtime class in its own Interface Definition Language (IDL) (.idl) file, in order to optimize build performance when you edit an IDL file, and for logical correspondence of an IDL file to its generated source code files.

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
A class declaration may also specify a list of interfaces that the class
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
initialize an instance of a class.

A constructor is declared like an instance method (but with no return
type), and with the same name as the containing class.

Instance constructors can be overloaded. For example, the **Test** class below declares three instance constructors; one with no parameters, one that
takes an **Int32** parameter, and one that takes two **Double** parameters.

```idl
runtimeclass Test
{
    Test();
    Test(Int32 x);
    Test(Double x, Double y);
}
```

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

The Windows Runtime doesn't support write-only properties. But you can specify only the `set` keyword to revise an existing read-only property into a read-write property. Take this version of **Area** as an example.

```idl
unsealed runtimeclass Area
{
    ...
    Color SurfaceColor { get; };
}
```

If you want subsequently to make the **SurfaceColor** property read-write, and you don't need to maintain binary compatibility with prior declarations of **Area** (for example, the **Area** class is a type in an application that you
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

##### Instance and static properties
Similar to fields and methods, MIDL 3.0 supports both instance
properties and static properties. Static properties are declared with
the `static` modifier, and instance properties are declared without it.

#### Methods
A *method* is a member that implements a computation or action that
can be performed by an instance of the class, or by the class itself. A *static method* is accessed through the class. An *instance method* is accessed through an instance of the class.

A method has a (possibly empty) list of *parameters*, which
represent values or variable references passed to the method. A method also has a *return type*, which specifies the type of the value computed and
returned by the method. A method's return type is `void` if it doesn't
return a value.

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
A method declared with a `static` modifier is a *static method*. A
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
handler.

### Delegates
A *delegate type* specifies a method with a particular parameter list and return type. A single instance of an event can contain any number of references to instances of its delegate type.

A delegate makes it possible to treat
methods as entities that can be assigned to variables and passed as
parameters. Delegates are similar to the concept of function pointers
found in some other languages. But, unlike function pointers, delegates
are object-oriented and type-safe.

If we don't want to use the [**WindowSizeChangedEventHandler**](/uwp/api/windows.ui.xaml.windowsizechangedeventhandler) delegate type from the platform, then we can declare our own delegate type.

```idl
delegate void SizeChangedHandler(Object sender, Windows.UI.Core.WindowSizeChangedEventArgs args);
```

An instance of our **SizeChangedHandler** delegate type can reference any
method that takes two arguments (an **Object**, and a [**WindowSizeChangedEventArgs**](/uwp/api/windows.ui.core.windowsizechangedeventargs)), and
returns void. After we've discussed *structs*, you'll also be able to replace the **WindowSizeChangedEventArgs** parameter with an *event args* type of your own.

An interesting and useful property of a delegate is that it doesn't
know or care about the class of the method it references; all that
matters is that the referenced method has the same parameters and return
type as the delegate.

### Structs
*Structs* are data structures that can contain data members. But,
unlike a class, a struct is a value type.

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

### Enums
An *enum type* is a distinct value type with a set of named
constants. The following example declares and uses an enum type named
**Color** with three constant values: **Red**, **Green**, and **Blue**.

```idl
enum Color
{
    Red,
    Green,
    Blue
}
```

Each enum type has a corresponding integral type called the
*underlying type* of the enum type. The underlying type of an enum
is either **Int32** or **UInt32**.

When an enum is a *Flags* enum (that is, it has the `[Flags]` attribute
applied), the underlying type of the enum is **UInt32**. When the `[Flags]` attribute is not present, the underlying type of the enum is **Int32**.

An enum type's storage format and range of possible values are
determined by its underlying type. The set of values that an enum type
can take on is not limited by its declared enum members.

The following example declares an enum type named **Alignment**, with an
underlying type of **Int32**.

```idl
enum Alignment
{
    Left = -1,
    Center = 0,
    Right = 1
}
```

An enum member declaration can include a constant expression that
specifies the value of the member. The constant value for each enum
member must be in the range of the underlying type of the enum. When an
enum member declaration doesn't explicitly specify a value, the member
is given the value zero (if it is the first member in the enum type), or
the value of the textually preceding enum member plus one.

The following example declares an enum type named **Permissions**, with an
underlying type of **UInt32**.

```idl
[Flags]
enum Permissions
{
    None = 0x0000,
    Camera = 0x0001,
    Microphone = 0x0002
}
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

The next example declares a **HelpAttribute** attribute, which can be
placed on program entities to provide links to their associated
documentation.

```idl
attribute HelpAttribute
{
    HelpAttribute(String classUri);
    String ClassUri { get; };
    String MemberTopic { get; set; };
}
```

An attributes can be applied by giving its name, along with any
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
declaration by using a scope block following the
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
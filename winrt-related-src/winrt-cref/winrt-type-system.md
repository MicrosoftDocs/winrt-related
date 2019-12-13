---
title: The Windows Runtime (WinRT) type system
description: The Windows Runtime (WinRT) type system.


ms.topic: reference
ms.date: 01/25/2019
keywords: windows 10, uwp, winrt, type, system
ms.localizationpriority: medium
---

# The Windows Runtime (WinRT) type system

## General notes

All types&mdash;except for the fundamental types&mdash;must be contained within a namespace. It's not valid for a type to be in the global namespace.

Types provided by Windows are all contained under the **Windows.\*** namespace. WinRT types that are not provided by Windows (including WinRT types that are provided by other parts of Microsoft) must live in a namespace other than **Windows.\***.

With the exception of interfaces, all WinRT types must have public visibility. WinRT interfaces may optionally have private visibility. All other user-defined WinRT types (structs, classes, enums, delegates, attributes) must have public visibility.

WinRT does not support nested types. No WinRT type can enclose another type; no WinRT type can be nested inside another type.

Not all aspects of the WinRT type system are available to you, as a third-party developer.

- WinRT supports parameterization of interfaces and delegates. However, in this release WinRT does not support definition of parameterized types by 3rd parties. Only the parameterized types included in the system in the Windows.* namespace are supported.

- WinRT support class composition as a runtime inheritance mechanism. However, in this release WinRT does not support definition of a root composable class. Only the root composable classes included in the system in the **Windows.\*** namespace are supported.

WinRT namespaces and type names are case-preserving, but insensitive, similar to the Windows File System and the Windows Registry. This means that you can't have namespaces or type names that vary only by case. For example, you can't have both **Foo.SomeType** and **foo.AnotherType**, nor can you have both **Foo.SomeType** and **Foo.someType**.

A WinRT identifier must conform to the following grammar. Note that only characters defined in Unicode 3.0 and earlier are supported.

    identifier-or-keyword: 
        identifier-start-character   identifier-continuation-characters* 
    identifier-start-character: 
        letter-character
        underscore (U+005F) 
    identifier-continuation-characters: 
        identifier-continuation-character
        identifier-continuation-characters   identifier-continuation-character 
    identifier-continuation-character: 
        identifier-start-character 
        decimal-digit-character
        connecting-character
        combining-character
        formatting-character 
    letter-character: 
        A Unicode 3.0 character of classes Lu, Ll, Lt, Lm, Lo, or Nl 
    combining-character: 
        A Unicode 3.0 character of classes Mn or Mc 
    decimal-digit-character: 
        A Unicode 3.0 character of the class Nd 
    connecting-character: 
        A Unicode 3.0 character of the class Pc 
    formatting-character: 
        Zero Width Non-Joiner (U+200C)
        Zero Width Joiner (U+200D)

## Parameterized types
WinRT supports type parameterization of interfaces and delegates. The parameterized types permit a family of interfaces to be defined that may be processed polymorphically in programming languages that support parametric polymorphism.

A parameterized type instantiation occurs when a parameterized type is specified with an argument list of types in a type context, such as a method parameter position. For example, `HRESULT foo(X<Y> x)` instantiates the parameterized type named by **X** with the type **Y** as its first and only type argument.

An unparameterized WinRT interface or delegate is assigned a GUID to uniquely identify the underlying interface as distinct from other interfaces on the same object. A parameterized interface (for example, `IVector<T>`) or delegate (for example, `EventHandler<T>`) is instead assigned a parameterized interface ID (PIID), which is a GUID uniquely identifying this parameterized type. This is not an IID. This GUID is used in generating IIDs for parameterized type instances (for example, `IVector<int>`).

### Parameterized type argument list
These WinRT types are permitted to appear in the argument list for a parameterized type.
* WinRT fundamental types (for example, **Boolean**, **Int32**, **String**, **Guid**, etc.)
* WinRT enums
* WinRT structs 
* WinRT interfaces 
* WinRT delegates
* WinRT runtime classes
* Other parameterized type instantiations (for example, `IVector<IVector<int>>`)
Any other type is forbidden from appearing in a parameterized type argument list. For example, arrays.

### Parameterized type instances
A parameterized type instance can appear in any context that a non-parameterized type can appear. A parameterized interface instance may be used anywhere an interface may be used, such as in the list of interfaces implemented by a runtime class. A parameterized delegate instance may be used anywhere a delegate may be used, such as in the definition of an event.

A parameterized type parameter can appear: in the parameterized interface or delegate definition; or, any place that a normal type can normally appear. If a parameter appears where only an interface can appear, that parameter is restricted to be an interface. If a parameter appears in a context where any type can appear, that parameter is not restricted; and so forth. Arguments to parameterized type instances must meet all such restrictions.

### Guid generation for parameterized types
The guid generation algorithm must meet these requirements.

- When a parameterized type is instantiated twice with the same arguments, both instantiations must be assigned the same interface or delegate body, and the same IID.
- If two different parameterized types are instantiated, even with the same arguments, it must be statistically unlikely that they are assigned the same IID.
- If a parameterized type is instantiated twice, but with different arguments, it must be statistically unlikely that the two instantiations are assigned the same IID.

> [!NOTE]
> It's not permitted for a parameterized type to be instantiated with the same instantiation as an argument, or as an argument to any other parameterized type that appears in the argument list (that is, circular instantiation). For example, if `X = Foo<Y>`, and `Y = Foo<X>`, non-circularity has been violated. However, if `X = Foo<Y>` and `Y = Foo<int>`, then non-circularity has been maintained.

The instantiation algorithm is as follows.
1. Each parameterized type is assigned a parameterized interface ID by its author&mdash;abbreviated PIID. Note that a PIID is not an IIDs, nor is it passed as an argument to QueryInterface. The author must ensure that the PIID is unique to the parameterized type.
2. The type signature for a base type is an ASCII octet string (see the table below). For example, **Int32** is "i4".
3. The type signature for an interface that is not a parameterized interface instance is its IID encoded in ASCII in dashed form, and delimited by curly braces. For example, "{00000000-0000-0000-0000-000000000000}".
4. The type signature for a delegate that is not a parameterized delegate instance is the string "delegate", and then the IID as with interfaces. The detailed grammar appears next.
5. The guid for a parameterized type is computed according to this grammar.
    - signature_octets => guid_to_octets(wrt_pinterface_namespace) string_to_utf8_octets(ptype_instance_signature)

        wrt_pinterface_namespace => "11f47ad5-7b73-42c0-abae-878b1e16adee"

        ptype_instance_signature => pinterface_instance_signature | pdelegate_instance_ signature

        pinterface_instance _signature => "pinterface(" piid_guid  ";" args ")"

        pdelegate_instance _signature => "pinterface(" piid_guid ";" args ")"

        piid_guid => guid

        args => arg | arg ";" args

        arg => type_signature

        type_signature => base_type_identifer | com_interface_signature | interface _signature | delegate_signature  | interface_group_signature | runtime_class_signature | struct_signature | enum_signature | pinterface_instance_signature | pdelegate_instance_signature
        com_interface_signature => "cinterface(IInspectable)"

        base_type_identifier is defined below

        interface_signature => guid

        interface_group_signature => "ig(" interface_group_name ";" default_interface ")"

        runtime_class_signature => "rc(" runtime_class_name ";" default_interface ")"

        default_interface => type_signature

        struct_signature => "struct(" struct_name ";" args ")"

        enum_signature => "enum(" enum_name ";" enum_underlying_type ")"

        enum_underlying_type => type_signature

        delegate_signature => "delegate(" guid ")"

        guid => "{" dashed_hex "}"

        dashed_hex is the format that uuidgen writes in when passed no arguments.

            dashed_hex => hex{8} "-" hex{4} "-" hex{4} "-" hex{4} "-" hex{12}

            hex => [0-9a-f]

    - according to UUID rfc 4122, compute the ver 5 sha-1 generated hash of signature_octets&mdash;this uses a single winrt pinterface/pintergroup guid as the namespace as described in rfc 4122/4.3, and the signature of the pinterface/pintergroup and the args it is instantiated with as the name string.
    - the pinterface instantiation is assigned this guid, and the signature from 4.
6. When a p-type instantiation is passed as an argument to anther pinterface, the signature computed by step 3 is used as the type signature in  grammar element 'pinterface_instance_signature' or 'pdelegate_instance_signature', as appropriate.

These names are used for base types when they appear.

- **UInt8** maps to "u1"
- **Int32** maps to "i4"
- **UInt32** maps to "u4"
- **Int64** maps to "i8"
- **UInt64** maps to "u8"
- **Single** maps to "f4"
- **Double** maps to "f8"
- **Boolean** maps to "b1"
    - Note that, in order to get **Boolean** type parameter support, you need to add `/Yc:wchar_t` to enable **wchar_t** as a built-in type.
- **Char16** maps to "c2"
- **String** maps to "string"
- **Guid** maps to "g16"

The above names are case sensitive. With the exception of **String**, the type name uses a single character to suggest the kind of data, followed by its size in bytes. These names were chosen: to be concise (to avoid large sizes in struct type signatures); to not appear confusingly similar to either the WinRT name, the RIDL name, nor the language projection name for any type; and still to remain roughly human-readable.

For enum_type_signature, the only valid ‘underlying_type’ value is that of **Int32** or **UInt32**.

For struct_type_signature, args is an in-order list of type_signatures for the fields of the struct. These may be base types, or other struct types.

Struct_name and enum_name are namespace-qualified, using period "." as delimiters. For example, "namespace X { struct A{ int; }; }" becomes "struct(X.A;i4)".

Default_interface must be the interface, p-interface instance, delegate, or p-delegate instance that was specified as default in the runtime class or interface group body, using the IDL '[default]' attribute.

Note that custom attributes are ignored; presumed to have no effect on marshaling.

## Versioning
All WinRT types except fundamental types must have a Version attribute. Language projections use the Version attribute info to enable backward compatibility, and for light-up scenarios. Third-party types must include a Version attribute, but it must be ignored by language projections. Third-party WinRT components are exclusively packaged in the app, so they can never change version independently of the app itself.

The Version attribute may optionally be applied to interface members (methods, properties, and events). This is intended for high-level class authoring in C#/VB and C++/CX. Version attributes on interface members, even Windows system interface members, must be ignored at runtime by language projections.

The Version attribute includes an unsigned 32-bit integer constructor parameter. For Windows WinRT types, this value is the NTDDI value for the version of Windows the associated type construct was first defined in. For third-party types, the meaning of this value is up to the type's author.

Windows system structs, delegates, and interfaces are immutable once defined. They may never be modified in any subsequent Windows release.

Windows system enums and runtime classes are additively versionable. Enums may add new enum values in subsequent Windows releases. Classes may add new implemented interfaces (including static, activation factory, composition factory, overridable, and protected interfaces) in subsequent Windows releases. Further details on additive versioning are included in the sections for enums and runtime classes.

## Namespaces
A namespace is a naming scope used to organize code, and to avoid naming collisions. All named types in the WinRT type system (enums, structs, delegates, interfaces, and runtime classes) live in a namespace. A namespace can contain other namespaces.

## Fundamental types
The WinRT Type system includes a core set of built-in primitive types.

|WinRT type|Type description|
|-|-|
|Int16|a 16-bit signed integer|
|Int32|a 32-bit signed integer|
|Int64|a 64-bit signed integer|
|UInt8|an 8-bit unsigned integer|
|UInt16|a 16-bit unsigned integer|
|UInt32|a 32-bit unsigned integer|
|UInt64|a 64-bit unsigned integer|
|Single|a 32-bit IEEE 754 floating point number|
|Double|a 64-bit IEEE 754 floating point number|
|Char16|a 16-bit non-numeric value representing a UTF-16 code unit|
|Boolean|an 8-bit Boolean value|
|String|an immutable sequence of **Char16** used to represent text|
|Guid|A 128-bit standard Guid|

## Enums
An enum type is a distinct value type with a set of named constants.

Each enum type has a corresponding integral type called the underlying type of the enum type. The only legal enum underlying types in WinRT are **Int32** and **UInt32**.

An enum with an underlying type of **UInt32** must carry the FlagsAttribute. An enum with an underlying type of **Int32** must not carry the FlagsAttribute.

An enum must have public visibility.

### Enum versioning
An enum is additively versionable. Subsequent versions of a given enum may add values (also known as named constants). Pre-existing values may not be removed or changed. Enum values optionally carry the VersionAttribute to distinguish when specific values were added to the enum type. Enum values without a VersionAttribute are considered to have the same version value as the enclosing enum type.

## Structs
A struct is a record type with one or more fields. Structs are always passed and returned by value. Struct fields may only be enums, structs, and fundamental types (including strings).

Structs must have public visibility.

A struct must have at least one field. All of a struct's fields must be public.

A struct cannot be generic nor parameterized.

## Interfaces
An interface is a contract that consists of a group of related type members whose usage is defined but whose implementation is not. An interface definition specifies the interface's members&mdash;methods, properties, and events. There is no implementation associated with an interface.

Non-parameterized interfaces must have a unique interface ID (aka IID) specified via a GuidAttribute. A parameterized interface must have a unique parameterized interface ID (also known as a PIID) specified via a GuidAttribute. The PIID is used to generate an IID for a specific parameterized interface instance via the algorithm specified above.

An interface may have public or private visibility. This reflects the fact that some interfaces represent shared contracts implemented by multiple WinRT classes, while other interfaces represent members implemented by a single WinRT class. A private-visibility interface must specify the WinRT class it is exclusive to via the ExclusiveToAttribute. Private interfaces may only be implemented by the WinRT class specified in the ExclusiveToAttribute.

### IInspectable and IUnknown
All WinRT interfaces must inherit directly from IInspectable, which in turn inherits from IUnknown. IUnknown defines three methods: QueryInterface, AddRef, and Release as per traditional COM usage. IInspectable defines three methods in addition to the IUnknown methods: GetIids, GetRuntimeClassName, and GetTrustLevel. These three methods allow the object's client to retrieve information about the object. In particular, IInspectable.GetRuntimeClassName enables an object's client to retrieve a WinRT typename that can be resolved in metadata to enable language projection.

### Interface requires
An interface may specify that it requires one or more other interfaces that must be implemented on any object that implements the interface in question. For example, if **IButton** requires **IControl**, then any class implementing **IButton** would also need to implement **IControl**.

Adding new functionality by implementing new interfaces that inherit from existing interfaces (for example, **IFoo2** inherits from **IFoo**) is not allowed.

### Parameterized interfaces
Interfaces support type parameterization. A parameterized interface definition specifies a type parameter list in addition to the list of interface members and required interfaces. A required interface of a parameterized interface may share the same type argument list, such that a single type argument is used to specify the parameterized instance of both the interface and the interface that it requires (for example, `IVector<T> requires IIterable<T>`). The signature of any member (that is, method, property, or event) of a parameterized interface may reference a type from the parameterized interface's type arguments list (for example, `IVector<T>.SetAt([in] UInt32 index, [in] T value)`).

Third-parties cannot define new parameterized interfaces. Only the parameterized interfaces defined by the system are supported.

## Delegates
A delegate is a WinRT type that acts as a type-safe function pointer. A delegate is essentially a simple WinRT object that exposes a single interface that inherits from **IUnknown**, and defines a single method named **Invoke**. Invoking the delegate in turn invokes the method it references. Delegates are often (but not exclusively) used for defining WinRT events.

A WinRT delegate is a named type, and defines a method signature. Delegate method signatures follow the same rules for parameters as interface methods do. The signature and parameter names of the **Invoke** method must match the definition of the delegate.

Like interfaces, non-parameterized delegates must have a unique interface ID (aka IID) specified via a GuidAttribute. The IID of the delegate is used as the IID of the single method interface used to implement the delegate. Parameterized delegates must have a unique parameterized interface ID (also known as a PIID) specified via a GuidAttribute. The PIID is used to generate an IID for a specific parameterized delegate instance via the algorithm specified above.

A delegate must have public visibility.

### IUnknown
Note that, unlike WinRT interfaces, delegates implement **IUnknown**, but not **IInspectable**. This means that they cannot be inspected for type information at runtime.

### Parameterized delegates
Delegates support type parameterization. A parameterized delegate definition specifies a type parameter list in addition to the traditional method signature as specified above. In the method signature, any parameter may be specified as one of the types from the parameterized delegates' type arguments list.

Third-parties cannot define new parameterized delegates. Only the parameterized delegates defined by the system are supported.

## Interface members
WinRT interfaces support three types of members: methods, properties, and events. Interfaces may not have data fields.

### Methods
WinRT interfaces support methods that take zero or more parameters, and that return an **HRESULT** indicating the success or failure of the method call. A method may optionally indicate a single out parameter to be projected as the return value in exception-based languages. This return value out parameter, if specified, must be the last parameter in the method signature.

A method must have public visibility.

A method may not use variable numbers of arguments. A method may not have optional parameters, nor parameters with default values.

A method may not be parameterized. Parameterized delegates and methods of parameterized interfaces may use type parameters of the containing type in the method signature.

### Parameters
All method parameters except array length parameters (described below) must have a name and a type. Note that return values must specify a name just like parameters do. Method parameter names, including the return type name, must be unique within the scope of the method.

Only parameters for parameterized delegates and members of parameterized interfaces may specify a parameterized type for the parameter type. Methods may not be individually parameterized. Parameters may always specify parameterized type instances (for example, `IVector<int>`) as the parameter type.

All method parameters must be exclusively in or out parameters. In/out parameters are not supported.

While a method on a WinRT interface must return an **HRESULT**, a method may optionally indicate that its final out parameter is intended to be used as the return value when the method is projected into exception-based languages. Such parameters are known as [out, retval] parameters after the MIDL syntax used to declare them. When an [out, retval] parameter is specified, it must be the last parameter in the method signature.

Other than [out, retval] needing to appear at the end of the parameter list, there are no other ordering requirements for out parameters. 

#### Array parameters
WinRT methods support conformant array parameters. Arrays can never be used except as parameters. They cannot be stand-alone named types, and they cannot be used as a struct field type. Array parameters can be used as `in`, `out`, and `retval` parameters.

WinRT supports array parameters of most WinRT types including fundamental types (including string and guid), structs, enums, delegates, interfaces, and runtime classes. Arrays of other arrays are not allowed.

Because they are conformant, array parameters must always be immediately preceded in the parameter list by a parameter for the array size. The array size parameter must be a **UInt32**. The array size parameter does not have a name.

WinRT supports three different array-passing styles.

- PassArray. This style is used when the caller provides an array to the method. In this style, both the array size parameter and array parameter are both `in` parameters.
- FillArray. This style is used when the caller provides an array for the method to fill, up to a maximum array size. In this style, the array size parameter is an `in` parameter, while the array parameter is an `out` parameter. When using the FillArray style, the array parameter may optionally specify one of the other parameters as the array length parameter. Details below.
- ReceiveArray. This style is used when the caller receives an array that was allocated by the method. In this style, the array size parameter and the array parameter are both `out` parameters. Additionally, the array parameter is passed by reference (that is, **ArrayType\*\***, rather than **ArrayType\***).

> [!NOTE]
> The combination of an `out` array size parameter, but an `in` array parameter, is not valid in WinRT.

When an array parameter is used as an [out, retval] parameter, the array length parameter must be an `out` parameter&mdash;that is, only the ReceiveArray style is legal for `retval` arrays.

#### Array length parameter
A FillArray style array parameter may optionally specify another parameter as the array length parameter. Where the required array size parameter specifies the maximum number of elements in an array provided by the caller, the array length parameter specifies the number of elements that were actually filled in by the callee.

The array length parameter is specified with the LengthIs attribute on the array parameter.

### Method overloading
Within the scope of a single interface, more than one method may have the same name. Methods with the same name on an interface must have unique signatures. Properties and events can't be overloaded.

WinRT supports overloading on parameter types, but favors overloading on the number of input parameters&mdash;also known as the method's *arity*. This is done in order to support dynamic, weakly-typed languages (such as JavaScript).

When an interface has multiple methods of the same name and number of input parameters, exactly one of those methods must be marked as the default. Of all the overloaded methods with the same name and number of input parameters, only the method marked as the default will be projected by a dynamic, weakly typed language. If there is only a single overloaded method of a given name and number of input parameters, marking it as the default is valid, but not required.

For the purposes of determining a method's arity, array parameters and their required length parameter are consider a single parameter. The PassArray and FillArray styles are considered a single input parameter, while the ReceiveArray style is considered a single output parameter.

When multiple methods on an interface have the same name, a unique name for each colliding method must be stored in an OverloadAttribute attached to the method. Default overloaded methods carry the DefaultOverloadAttribute.

#### Operator overloading
WinRT does not support operator overloading. Methods may not be named using the special operator names such as op_Addition that are specified in the ECMA 335 CLI spec, partition I, section 10.3.

### Properties
A property is a pair of get/set methods with matching name and type that appear in some language projections as fields rather than methods.

A property and its get/set methods must have public visibility.

A property must have a `get` method. A property getter method has no parameters, and returns a value of the property type. A property with only a `get` method is called a read-only property.

A property may optionally have a `set` method. A property setter method has a single parameter of the property type, and returns void. A property with both a `get` and a `set` method is called a read/write property.

Properties may not be parameterized. Properties from parameterized interfaces may use type parameters of the containing type as the property type.

### Events
An event is a pair of add/remove listener methods with matching name and delegate type. Events are a mechanism for the interface to notify interested parties when something of significance happens.

An event and its add/remove listener methods must have public visibility.

An event `add` listener method has a single parameter of the event delegate type, and returns a **Windows.Foundation.EventRegistrationToken**. An event `remove` listener method has a single parameter of the **Windows.Foundation.EventRegistrationToken** type, and returns void.

Events may not be parameterized. Events from parameterized interfaces may use type parameters of the containing type as the event delegate type.

## Runtime classes
WinRT allows you to define a class. A class must implement one or more interfaces. A class cannot implement type members directly (that is, it can't define its own methods, properties, nor events). A class must provide an implementation of all the members of all the interfaces it implements.

There are several different types of interfaces, which are described in detail below.

- Member interfaces (including protected and overridable interfaces)
- Static interfaces
- Activation factory interfaces
- Composition factory interfaces

Runtime classes cannot be parameterized. A runtime class may implement a parameterized interface instance (that is, a parameterized interface with all its type parameters specified) anywhere it would typically accept a non-parameterized interface. 

A runtime class must have public visibility.

A runtime class may only implement interfaces that are not exclusive (that is, don’t carry the exclusiveTo attribute) or that are exclusive to the runtime class in question. A runtime class may not implement interfaces that are exclusive to a different runtime class. There is one exception to this rule&mdash;a composable class may implement interfaces that are exclusive to a class in its derivation chain that is marked as overridable. Details on overridable interfaces to follow.

### Member interface
A runtime class may implement zero or more member interfaces. Member interfaces enable classes to expose functionality that is associated with instances of the class. A runtime class specifies a list of the member interfaces it implements. Entries in the list of member interfaces implemented by a runtime class may optionally carry version information. Details on runtime class versioning to follow.

Member interfaces are implemented directly on instances of the runtime class.

Runtime classes that implement one or more member interfaces must specify one of the member interfaces to be the default interface. Runtime classes that implement zero member interfaces do not specify a default interface.

### Static interfaces
WinRT classes may specify zero or more static interfaces. Static interfaces enable classes to expose functionality that's associated with the class itself, rather than with specific instances of the class.

A class must specify at least one member or static interface. A class with no member and no static interfaces is invalid.

Static interfaces are specified via a StaticAttribute associated with the runtime class. StaticAttribute carries a reference the static interface reference as well as version information. Details on runtime class versioning to follow.

While static interfaces are declared as part of the runtime class, they are actually not implemented on class instances themselves. Rather, they are implemented on the class's activation factory. Details on activation factories to follow.

### Activation 
Runtime classes optionally support activation&mdash;the ability of the system to produce instances of a specified class. Classes must implement at least one member interface in order to support activation.

WinRT defines three activation mechanisms: direct activation (with no constructor parameters), factory activation (with one or more constructor parameters), and composition activation. Non-composable classes may support either direct and/or factory activation. Composable classes only support composable activation. Details on composition and composable activation to follow.

Classes that support direct activation are activated by calling the IActivationFactory.ActivateInstance method on the class's activation factory. This method takes no parameters, and returns a newly activated instance of the runtime class. Details on activation factories to follow.

Classes that support factory activation define one or more factory interfaces, which each in turn define one or more factory methods. These factory interfaces are implemented on the class's activation factory.

Factory methods take one or more `in` parameters, and must return a newly activated instance of the runtime class. Other `out` parameters beyond the newly activated class instance are not allowed. Factory methods must take one or more parameters&mdash;parameterless factory activation is not allowed. Direct activation must be used for parameterless activation.

Classes that support either direct or factory activation are marked with the ActivatableAttribute. The ActivatableAttribute carries version information (details on runtime class versioning to follow) as well as an optional reference to the factory interface. Classes can be marked with multiple ActivatableAttributes&mdash;at most one for default activation, plus one for every factory interface implemented by the class's activation factory. Classes marked with the ActivatableAttribute may not also be marked with the ComposableAttribute. Details on composition to follow.

### Composition
Runtime classes optionally support composition&mdash;the ability for multiple class instances to be combined into what appears to be a single object from the outside. WinRT uses composition as a form of runtime class inheritance.

WinRT classes can optionally compose a single composable base class, which in turn may compose a single composable base class, etc. A class does not itself need to be composable in order to compose a composable base class. Classes may only compose with a composable class as a base class. A composable class is not required to compose another composable class (that is, it may be the root of the hierarchy). Circular graphs of composition (such as A composes B, which composes A) are not allowed.

At runtime, a composing class is an aggregation of WinRT objects&mdash;one for each object in the composition chain. These aggregated objects delegate identity and lifetime to the originally activated object in the composition chain (called the controlling object). Every object in the chain holds a non-delegating **IInspectable** pointer to the class it composes in order to call methods on composed base class interfaces, including methods on protected interfaces. Every object in the chain has a pointer to the controlling class for delegating lifetime and identity as well as in order to call methods on overridable interfaces. Details on protected and overridable interfaces to follow.

Let's take the example that **Button** composes **Control**, which in turn composes **UIElement**. In that example, an instance of **Button** aggregates a **Control** instance, which in turn aggregates a **UIElement** instance. All three objects have a reference to the **Button** object for controlling lifetime and identity as well as for querying for overridable interfaces. Each object has an **IInspectable** pointer to the object that it composes (**Button** holds a pointer to **Control**; **Control** holds a pointer to **UIElement**) in order to be able to call methods on interfaces implemented on composed classes, including protected interfaces. 

A class may not implement any interfaces defined on the class it composes, nor any class in the composition chain, unless the interface is marked as overridable in the composable class. Details on overridable interfaces to follow.

A composable class must be marked with one or more ComposableAttributes. The ComposableAttribute carries a reference to the composition factory interface&mdash;whether the factory methods on the composition factory interface can be used for controlling object activation or not&mdash;as well as version information. Details on composition factory interfaces and versioning to follow. A class can be marked with multiple ComposableAttributes&mdash;one for every composition factory interface implemented by the class's activation factory.

The JavaScript language projection doesn't support class composition. As such, composable classes, and classes that compose composable classes, should be marked with the WebHostHiddenAttribute indicating that JavaScript should not attempt to project these types.

Third-parties can only define classes that compose other composable classes. You may not define your own composable root class.

#### Composable activation
A composable class must define one or more composition factory interfaces, which in turn implement one or more composition factory methods. Composition factory interfaces are implemented on the class's activation factory. Details on activation factories to follow.

A composition factory interface is used to create composable instances of the class. A composable factory interface declares zero or more composable factory methods that can be used to activate instances of the class for composition purposes. Note that it is legal to have a composable factory interface with zero factory methods. This implies that the class can be used for composition, but that third-parties may not directly compose the class&mdash;the method(s) to create instances are internal only.

A composable class declares whether the factory methods on a given composition factory interface can be used to activate the class directly as a controlling object or not. Composable factory interfaces marked as public may be used to directly activate a class as a controlling object, as well as indirectly to activate a class as a composed object. Composable factory interfaces marked protected may only be used to indirectly activate a class as a composed object. Composable classes can always be activated as composed objects.

A composition factory interface must be `exclusiveto` the runtime class it is implemented by.

Like an activation factory method, a composition factory method must return an instance of the composable class. Additionally, a composition factory method has two additional parameters: the controlling **IInspectable\*** [in] parameter, and the non-delegating **IInspectable\*\*** [out] parameter. A composition factory method may optionally have additional `in` parameters. If specified, the additional in parameters must occur at the beginning of the method signature, before the mandated parameters listed previously. A composition factory method may not have any additional `out` parameters beyond the non-delegating **IInspectable\*\*** and the return value parameters.

When a composable class is activated for composition (for example, **Control** or **UIElement** when a **Button** instance is activated), a pointer to the object that controls identity and lifetime is passed in via the controlling **IInspectable\*** [in] parameter. The composable factory method returns the newly activated instance as the return value. This instance delegates all identity and lifetime management functionality to the controlling **IInspectable\*** that was provided. Additionally, the composable factory method returns a pointer to a non-delegating **IInspectable\*** that the composing class can use to invoke methods on a composed class.

When a composable class is activated as a controlling class (for example, **Button** in the previous example), the same composable factory methods are used as for activation for composition. When activating a composable class directly, null is passed for the controlling **IInspectable\** parameter. This is an indicator to the composable class that it is being activated as a controlling class. When a controlling class creates the instance of the class it composes, it passes a reference to itself as the controlling **IInspectable\*** parameter. The composable factory method returns the controlling class instance as the return value. The non-delegating **IInspectable\*\*** [out] parameter is ignored by client code when activating a controlling composable class.

Building on the earlier **Button** -> **Control** -> **UIElement** example, the button class would be activating by calling one of its composition factory methods and passing null for the outer parameter. **Button** would in turn activate a **Control** instance, passing a reference to itself as the outer parameter. **Control** would in turn activate a **UIElement** instance, passing the outer reference it received as the outer parameter. The **UIElement** factory method would return to **Control** the newly created **UIElement** in the instance parameter, as well as a reference to **UIElement**'s non-delegating **IInspectable** in the inner parameter. The **Control** factory method would return to **Button** the newly created **Control** in the instance parameter as well as a reference to **Control**'s non-delegating **IInspectable** in the inner parameter. The **Button** composition factory would return to the calling code the newly created **Button** in the instance parameter, and null for the inner parameter.

It's possible for a class to be sometimes activated for composition, and other times activated as the controlling class. For example, if **RadioButton** composed **Button**, then **Button** would be activated for composition when a **RadioButton** was activated; but activated as the controlling class when **Button** was activated directly. In either case, the **Control** class that **Button** composes would be activated for composition.

#### Protected interfaces
A composable class may declare zero or more of its member interfaces to be protected. A non-composable class may not declare member interfaces to be protected. Only code in a class that composes a composable class (directly or indirectly) may query for and use interfaces that the composable class declares as protected. Code from outside the composition chain may not query for, nor use, interfaces that the composable class declares as protected.

For example, if **UIElement** declares a protected interface **IUIElementProtected**, then only classes that compose **UIElement**&mdash;including both direct (**Control**) and indirect (**Button**) composition&mdash;may query for and use the **IUIElementProtected** interface.

#### Overridable interfaces
A composable class may declare zero or more of its member interfaces to be overridable. An overridable interface may only be queried for, and used within, a composition chain&mdash;similar to the rules about accessing protected interfaces detailed previously. However, where a protected interface may only be implemented by the class that originally declared it, overridable interfaces may be re-implemented by classes that compose the class that implemented the overridable interface.

At runtime, any composable class code that leverages the overridable interface must QueryInterface for the interface via the controlling **IInspectable\*** pointer that is used for identity and lifetime delegation. This pointer returns the implementation of the overridable interface earliest in the composition chain (that is, closest to the controlling class instance). A class that wishes to access the overridable interfaces of the class it composes may do so via the non-delegating reference that a composable class holds to its composed class.

Let's take the example that **UIElement** declares an overridable interface **IUIElementOverridable**. In that case, classes that derive from **UIElement**, including both direct (**Control**) and indirect (**Button**) derivation, would be allowed to implement it. If code in **UIElement** needed to access functionality in **IUIElementOverridable**, then **UIElement** would query the controlling **IInspectable** to get the earliest implementation in the composition chain. If **Control** and **Button** both implemented **IUIElementOverridable**, then the **Button** implementation would be returned when the controlling **IInspectable** was queried. If **Button** wants to access its composed class functionality, it can use the non-delegating **IInspectable** that was returned from the composition factory method to query the base class for that interface.

### Activation factories
A runtime class optionally has an activation factory. A runtime class must have an activation factory if the class is activatable, composable, or has static interfaces. The activation factory for a class can be retrieved from the system at runtime via the **RoGetActivationFactory** Win32 function.

Activation Factories must implement the **IActivationFactory** interface. However, only classes that support direct activation provide an implementation of **IActivationFactory**'s single method **ActivateInstance**. Classes that don't support direct activation must return **E_NOTIMP**L from **IActivationFactory.ActivateInstance**.

The activation factory must implement all activation factory interfaces, composition factory interfaces, and static interfaces defined on the runtime class. 

There is no guarantee that language projections maintain a single activation factory instance for the lifetime of the factory. WinRT class authors who need to save long-lived information for static member access need to store it somewhere outside of the activation factory.

### Class-based projection
While WinRT is primarily an interface-based programming model under the hood, runtime classes provide a class-based programming model that is better aligned to modern, mainstream, object-oriented (OO) programming languages. Language projections are expected to project a runtime class as a single entity, rather than as a bag of interfaces that the developer has to deal with separately.

To achieve this class-based model, language projections are expected to project type members from a class's member interfaces as direct class members. Language projections are expected to project type members from a class's static interfaces as static class members. Finally, language projections are expected to project activation methods (direct activation as well as interfaces from factory and composable factory interfaces) as class constructors.

To assist in this class-based projection, metadata for runtime classes specify a class member for all the methods, properties, and events from every interface they implement. Every class member is explicitly tied back to the interface member where it was originally defined. This allows language projections to expose the class as a single entity, handling all the interface querying and reference counting under the covers on behalf of the developer.

By default, every implemented interface member is projected as a class member. However, because runtime classes can implement multiple independent interfaces and version over time (versioning details to follow), it is possible for there to be name collisions for members defined on different interfaces implemented by a single runtime class.

When collisions occur, default class member projection is impossible. If collisions occur across interfaces added in separate versions, the colliding member from the earliest version is projected as a class member. When collisions occur across interfaces added in the same version, none of the colliding members are projected as class members. Note, methods with colliding names are permitted so long as all the versions are of different *arity* as described in [Method overloading](#method-overloading).

Interface members that are not projected as class members must be made available to developers. Typically, this is a done by a casting or dynamic lookup operator, allowing the developer to specify the specific interface and method they want to invoke.

In order to resolve method name collisions, runtime classes may specify alternative names for methods on the member and static interfaces they implement. This alternative name is used by the language projection to provide disambiguated access to colliding method names from a class instance. While the runtime class may provide an alternative method name, the method signature, parameters, and any attributes attached to the method or its attributes must still match the original interface definition exactly.

Since direct activation, factory methods, and composition factory methods are projected as class constructors, they are all projected on the runtime class as if they have the same name. All methods across all factory interfaces must have unique signatures, should favor *arity*-based overloading over type-based overloading, and must use the DefaultOverloadAttribute to disambiguate factory methods of the same arity.

### Class versioning
Runtime classes are additively versionable. Subsequent versions of a given runtime class may specify additional interfaces of all types, with further details on individual interface types below. Pre-existing interfaces specified by a class may never be removed or changed without breaking backwards compatibility.

#### Member interface versioning
Member interfaces on runtime classes are additively versionable. Subsequent versions of a given runtime class may implement additional member interfaces, even if the class had never implemented member interfaces previously. Subsequent versions of a given composable runtime class may implement additional protected and overridable interfaces.

Interfaces implemented by a runtime class optionally carry the VersionAttribute to distinguish when specific interfaces were added to the runtime class type. Interface implementation values without a VersionAttribute are considered to have the same version value as the enclosing runtime class type.

#### Static interface versioning
Static interfaces on runtime classes are additively versionable. Subsequent versions of a given runtime class may implement additional static interfaces, even if the class had never implemented static interfaces previously.

The StaticAttribute includes a **UInt32** parameter for version number, which defines the version of Windows that added that activation support.

#### Activation versioning
Activation support for runtime classes is additively versionable. Subsequent versions of a given runtime class may implement additional activation mechanisms, even if the class had never implemented an activation mechanism. Note, composable classes are not activatable, and thus may not add activation support.

Note that a class that supports direct activation may only add new factory activation interfaces. A class that previously only supported factory activation may add direct activation support as well as new factory activation interfaces.

The ActivatableAttribute includes a **UInt32** parameter for version number. The version number for the ActivatableAttribute defines the version of Windows that added that activation support.

#### Composition versioning
Composition support for runtime classes is additively versionable. Subsequent versions of a given composable runtime class may implement additional composition mechanisms, provided the class was defined as composable when it was created. Composable classes may not add activation support.

The ComposableAttribute includes a **UInt32** parameter for version number. The version number for the ComposableAttribute defines the version of Windows that added that composition support.

## Custom attributes
WinRT supports the definition of custom metadata attributes. All constructs in the WinRT type system can carry custom metadata attributes. This includes all named types (enums, structs, delegates, interfaces, classes, etc.) as well as individual elements contained within type constructs (such as methods, parameters, etc.).

Custom attributes are named like other WinRT types. However, they are not activatable. They are purely a data construct.

Custom attributes define a data schema of either positional parameters or named fields. A custom attribute may not use both positional parameters and named fields&mdash;it must choose one or the other. The types of a custom attribute's parameters and fields are limited to the WinRT fundamental types, enums, and references to other WinRT types. No other parameter or field type is allowed.

Custom attributes that use positional parameters must define one or more valid sets of positional parameters. Each set must specify zero or more positional parameters. An instance of the custom attribute must specify a single set of positional parameters as well as data for each positional parameter in the selected set.

A custom attribute that uses named fields specifies zero fields with names and types. An instance of the custom attribute must specify the name/value pairs for the fields it wishes to specify. An instance may specify values for all, some, or none of the name/value pairs.

It's valid for an attribute to have neither positional parameters nor named fields.

A custom attribute must have public visibility.

An attribute may specify the types of WinRT type constructs that it may be associated with via the AttributeUsageAttribute.

Third-parties cannot define custom attributes. Only the custom attributes defined by the system are supported.

---

description: This topic describes how the MIDL 3.0 compiler synthesizes and adds interfaces, as necessary.
title: Synthesizing interfaces (MIDL 3.0)

ms.date: 01/30/2019
ms.topic: reference
keywords: windows 10, uwp, winrt, api, reference, idl, midl, 3.0, 3, midl3
ms.localizationpriority: medium
---

# Synthesizing interfaces (MIDL 3.0)

## Assigning members to interfaces

A Windows Runtime class operates in terms of interfaces. Interfaces were barely mentioned in most of the preceding examples, though, because they're typically an implementation detail that you don't need to control in most cases.

As a result, when your class description doesn't otherwise reference an
interface&mdash;but when one is needed to implement the class&mdash;the MIDL 3.0
compiler synthesizes and adds them, as necessary.

### Default constructor

When you declare a default constructor as a member of a class, the
compiler produces a Windows Runtime class that's default activatable.
At the implementation level, this means that the metadata describes
the class as default activatable, and the class factory for the
runtimeclass implements the [**IActivationFactory**](https://msdn.microsoft.com/en-us/library/br205779) interface.

```idl
runtimeclass Area
{
    Area();
    ...
}
```

In this case, **Area** is compiled with the metadata `[Activatable]` with a **Type** of `null`.

### Non-default constructor(s)

When you declare one or more non-default constructors as members of a
class, the compiler produces a Windows Runtime class that's
activatable, rather than default activatable. At the implementation
level, this means that the metadata will describe the class as
activatable and specify the interface containing the constructor
methods.

By default, this interface is named I&lt;*className*&gt;Factory, and
the class factory for the runtimeclass implements that interface. If this interface name is already in use, then the compiler appends an integer numeral suffix (starting with 2), until it locates an unused name.

```idl
runtimeclass Area
{
    Area(Int32 width, Int32 height);
    ...
}
```

In this case, the compiler

- synthesizes a factory interface named **IAreaFactory**,
- adds an `exclusiveto` attribute to the synthesized interface, specifying that the interface can only be referenced by the runtime class, and
- adds an `activatable` attribute to the runtime class indicating that clients can use **IAreaFactory** interface members to create instances of the class.

So, the MIDL above can be interpreted like this.

```idl
[exclusiveto(Area)]
interface IAreaFactory
{
    Area(Int32 width, Int32 height);
}

[activatable(IAreaFactory)]
runtimeclass Area
{
    ...
}
```

A class may contain both a default constructor and additional
non-default constructors.

```idl
runtimeclass Area
{
    Area();
    Area(Int32 width, Int32 height);
    ...
}
```

In that case, the MIDL can be interpreted like this; with both forms of the `activatable` attribute.

```idl
[exclusiveto(Area)]
interface IAreaFactory
{
    Area(Int32 width, Int32 height);
}

[activatable()]
[activatable(IAreaFactory)]
runtimeclass Area
{
    ...
}
```

### Instance members

In the example below, **Area** has members **Height** and **Width**.

```idl
runtimeclass Area : Windows.Foundation.IStringable
{
    Int32 Height;
    Int32 Width;
}
```

Those members are not part of any interface that **Area** implements. So, the compiler synthesizes an interface for them named, by default, I&lt;*className*&gt;. If this interface name is already in use, then the compiler appends an integer numeral suffix (starting with 2), until it locates an unused name.

In the case of the MIDL above, the compiler

- synthesizes the **IArea** interface,
- adds an `exclusiveto` attribute to the synthesized interface, specifying that the interface can only be referenced by the runtime class,
- specifies that the runtime class implements **IArea**, and
- makes the new interface the default interface for the runtime class if the class doesn't already have a default interface.

So, the MIDL above can be interpreted like this.

```idl
[exclusiveto(Area)]
interface IArea
{
    Int32 Height;
    Int32 Width;
}

runtimeclass Area : IArea, Windows.Foundation.IStringable
{
}
```

### Static members

In the example below, **Area** has the static member **NumberOfAreas**.

```idl
runtimeclass Area : Windows.Foundation.IStringable
{
    static Int32 NumberOfAreas { get; };
}
```

The static member is not part of any static interface that **Area** implements. So, the compiler synthesizes an interface for it named, by default, I&lt;*className*&gt;Statics. If this interface name is already in use, then the compiler appends an integer numeral suffix (starting with 2), until it locates an unused name.

In the case of the MIDL above, the compiler

- synthesizes the **IAreaStatics** interface,
- adds an `exclusiveto` attribute to the synthesized interface, specifying that the interface can only be referenced by the runtime class, and
- adds a `statics` attribute to the runtime class, specifying that the class factory implements **IAreaStatics**.

So, the MIDL above can be interpreted like this.

```idl
[exclusiveto(Area)]
interface IAreaStatics
{
    Int32 NumberOfAreas { get; };
}

[static(IAreaStatics)]
runtimeclass Area : Windows.Foundation.IStringable
{
}
```

### Protected members

In the example below, **Area** has the protected member **DoProtectedWork**.

```idl
runtimeclass Area : Windows.Foundation.IStringable
{
    protected void DoProtectedWork();
}
```

The protected member is not part of any protected interface that **Area** implements. So, the compiler synthesizes an interface for it named, by default, I&lt;*className*&gt;Protected. If this interface name is already in use, then the compiler appends an integer numeral suffix (starting with 2), until it locates an unused name.

In the case of the MIDL above, the compiler

- synthesizes the **IAreaProtected** interface,
- adds an `exclusiveto` attribute to the synthesized interface, specifying that the interface can only be referenced by the runtime class, and
- adds a `protected` attribute to the runtime class, specifying that the class implements the protected interface **IAreaProtected**.

So, the MIDL above can be interpreted like this.

```idl
[exclusiveto(Area)]
interface IAreaProtected
{
    void DoProtectedWork();
}

[protected(IAreaProtected)]
runtimeclass Area : Windows.Foundation.IStringable
{
}
```

### Overrideable members

In the example below, **Volume** (which derives from **Area**) has the overrideable member **DoOverrideableWork**.

```idl
runtimeclass Volume : Area
{
    overridable void DoOverrideableWork();
}
```

The overrideable member is not part of any overrideable interface that **Area** implements. So, the compiler synthesizes an interface for it named, by default, I&lt;*className*&gt;Overrides. If this interface name is already in use, then the compiler appends an integer numeral suffix (starting with 2), until it locates an unused name.

In the case of the MIDL above, the compiler

- synthesizes the **IAreaOverrides** interface,
- adds an `exclusiveto` attribute to the synthesized interface, specifying that the interface can only be referenced by the runtime class, and
- adds an `overrideable` attribute to the runtime class, specifying that the class implements the overrideable interface **IAreaOverrides**.

So, the MIDL above can be interpreted like this.

```idl
[exclusiveto(Area)]
interface IAreaOverrides
{
    void DoOverrideableWork();
}

[overrideable(IAreaOverrides)]
runtimeclass Area : Windows.Foundation.IStringable
{
}
```
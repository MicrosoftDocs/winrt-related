---
author: stevewhims
description: There are a number of pre-defined custom attributes that allow you to control the name and IID for compiler-synthesized interfaces.
title: Predefined attributes (MIDL 3.0)
ms.author: stwhi
manager: "markl"
ms.date: 04/03/2018
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, winrt, api, reference, idl, midl, 3.0
ms.localizationpriority: medium
---

# Predefined attributes (MIDL 3.0)
> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

There are a number of pre-defined custom attributes that allow you to control the name and interface identifier (IID) for compiler-synthesized interfaces. These attributes allow you to control the versioning and binary API of your
class at a fine-grained level.

If you're a component developer and/or a library author, then you may wish to use these attributes to ensure that your components remain binary-stable from one version to the next.

If you're an application developer, then in general you won't need to use these attributes because you'll recompile your application after revisioning your types.

## The `[constructor_name]` attribute
The `constructor_name` attribute specifies the name and IID of the
factory interface that contains the constructor members. See [Synthesizing interfaces](synthesizing-interfaces.md) for more info about factory interfaces.

> [!NOTE]
> A factory interface is only applicable to a sealed class with non-default constructors, or to an unsealed class with default and/or non-default constructors.

In the example below, the protected **Block** constructor is placed in the
**IBlockFactory** interface, and that interface has the specified IID.

```idl
[constructor_name("Windows.UI.Xaml.Documents.IBlockFactory", 07110532-4f59-4f3b-9ce5-25784c430507)]
...
unsealed runtimeclass Block : Windows.UI.Xaml.Documents.TextElement
{
	...
	protected Block();
	...
}
```

As a result, when your class description doesn't otherwise reference an
interface, but when one is needed to implement the class, the MIDL 3.0
compiler synthesizes and adds interfaces, as necessary.

## The `[method_name]` attribute
Every Windows Runtime interface has an equivalent Application Binary
Interface (ABI) interface. The ABI interface requires that all members
have unique names. There are two cases in MIDL 3.0 where members either
don't have a name, or don't have a unique name.

- constructors, and
- two or more overloaded methods.

In these cases, the MIDL 3.0 compiler synthesizes a unique
member name, as necessary.

By default, the compiler assigns constructor methods the names &lt;*className*&gt;, &lt;*className*&gt;1, &lt;*className*&gt;2, and so on for the equivalent methods in the ABI interface.

Similarly, for overloaded methods, for the first overloaded method (in
lexical order), the compiler uses the original method name for the
equivalent ABI interface method. Subsequent overloads receive the
original name plus a unique integer numeral suffix (increasing from 2).

You can override the compiler's default name assignment using the
`method_name` attribute.

In this next example, we instruct the compiler to use the name
**CreateInstance** for the **Block** default constructor member.

```idl
unsealed runtimeclass Block : Windows.UI.Xaml.Documents.TextElement
{
	...
	[method_name("CreateInstance")] protected Block();
	...
}
```

## The `[static_name]` attribute
The `static_name` attribute specifies the name and IID of the interface
that contains static members of the class.

In this next example, the `static_name` attribute applied to the runtimeclass
specifies the name and IID of the interface that contains all static
members of the class that are not otherwise assigned to an interface. So, **LineHeightProperty**, **LineStackingStrategyProperty**, **MarginProperty**, and **TextAlignmentProperty** are members of the
**IBlockStatics** interface.

However, **HorizontalTextAlignmentProperty** is a member of the
**IBlockStatics2** interface, because of the `static_name` attribute
encompassing that member.

```idl
[static_name("Windows.UI.Xaml.Documents.IBlockStatics", f86a8c34-8d18-4c53-aebd-91e610a5e010)]
...
unsealed runtimeclass Block : Windows.UI.Xaml.Documents.TextElement
{
	...
	static Windows.UI.Xaml.DependencyProperty LineHeightProperty{ get; };
	static Windows.UI.Xaml.DependencyProperty LineStackingStrategyProperty{ get; };
	static Windows.UI.Xaml.DependencyProperty MarginProperty{ get; };
	static Windows.UI.Xaml.DependencyProperty TextAlignmentProperty{ get; };

	[static_name("Windows.UI.Xaml.Documents.IBlockStatics2", af01a4d6-03e3-4cee-9b02-2bfc308b27a9)]
	{
		static Windows.UI.Xaml.DependencyProperty HorizontalTextAlignmentProperty{ get; };
	}
	...
}
```

## The `[interface_name]` attribute
The `interface_name` attribute specifies the name and IID of the
interface that contains the instance members if the class.

In the example below, the `interface_name` attribute applied to the
runtimeclass specifies the name and IID of the interface that contains
all instance members of the class that are not otherwise assigned to an
interface. So, **LineHeight**, **LineStackingStrategy**, **Margin**, and **TextAlignment** are members of the **IBlock** interface.

However, **HorizontalTextAlignment** is a member of the **IBlock2** interface,
because of the `interface_name` attribute encompassing that member.

```idl
[interface_name("Windows.UI.Xaml.Documents.IBlock", 4bce0016-dd47-4350-8cb0-e171600ac896)]
...
unsealed runtimeclass Block : Windows.UI.Xaml.Documents.TextElement
{
	...
	Double LineHeight;
	Windows.UI.Xaml.LineStackingStrategy LineStackingStrategy;
	Windows.UI.Xaml.Thickness Margin;
	Windows.UI.Xaml.TextAlignment TextAlignment;

	[interface_name("Windows.UI.Xaml.Documents.IBlock2", 5ec7bdf3-1333-4a92-8318-6caedc12ef89)]
	{
		Windows.UI.Xaml.TextAlignment HorizontalTextAlignment;
	}
	...
}
```

You can also use the `interface_name` attribute to force the generation of an interface. In the example below, **StateTriggerBase** has no need for **IStateTriggerBase**, and it's only the presence of the `interface_name` attribute that causes it to be generated.

```idl
[interface_name("Windows.UI.Xaml.IStateTriggerBase", 48b20698-af06-466c-8052-93666dde0e49)]
unsealed runtimeclass StateTriggerBase
{
	protected void SetActive(Boolean IsActive);
};
```

## The `[default_interface]` attribute
The `default_interface` attribute is used to force the generation of a default interface where one wouldn't otherwise be generated. In the example below, **StateTriggerBase** has no need for a default interface, and it's only the presence of the `default_interface` attribute that causes one (named **IStateTriggerBase**) to be generated.

```idl
[default_interface]
unsealed runtimeclass StateTriggerBase
{
	protected void SetActive(Boolean IsActive);
};
```

As a result, when your class description doesn't otherwise reference an
interface, but when one is needed to implement the class, the MIDL 3.0
compiler synthesizes and adds interfaces, as necessary.

## The `[contract]` attribute
You use the `contract` attribute to specify the name and version of the [API contract](/uwp/extension-sdks/device-families-overview) in which you first introduced the attributed type and/or member.

In this next example, we apply the `contract` attribute to the runtime class to indicate that we introduced the **Block** class in version 1 of the **Windows.Foundation.UniversalApiContract** API contract.

```idl
[contract(Windows.Foundation.UniversalApiContract, 1)]
unsealed runtimeclass Block : Windows.UI.Xaml.Documents.TextElement
{
	...
}
```

All members of that class (unless we say otherwise) are considered to be introduced in that same API contract name and version. But, consider this next example.

```idl
[contract(Windows.Foundation.UniversalApiContract, 1)]
unsealed runtimeclass Block : Windows.UI.Xaml.Documents.TextElement
{
	[method_name("CreateInstance")] protected Block();

	[contract(Windows.Foundation.UniversalApiContract, 5)]
	[interface_name("Windows.UI.Xaml.Documents.IBlock2", 5ec7bdf3-1333-4a92-8318-6caedc12ef89)]
	{
		Windows.UI.Xaml.TextAlignment HorizontalTextAlignment;
	}

	[contract(Windows.Foundation.UniversalApiContract, 5)]
	[static_name("Windows.UI.Xaml.Documents.IBlockStatics2", af01a4d6-03e3-4cee-9b02-2bfc308b27a9)]
	{
		static Windows.UI.Xaml.DependencyProperty HorizontalTextAlignmentProperty{ get; };
	}

	Double LineHeight;
	static Windows.UI.Xaml.DependencyProperty LineHeightProperty{ get; };
	Windows.UI.Xaml.LineStackingStrategy LineStackingStrategy;
	static Windows.UI.Xaml.DependencyProperty LineStackingStrategyProperty{ get; };
	Windows.UI.Xaml.Thickness Margin;
	static Windows.UI.Xaml.DependencyProperty MarginProperty{ get; };
	Windows.UI.Xaml.TextAlignment TextAlignment;
	static Windows.UI.Xaml.DependencyProperty TextAlignmentProperty{ get; };
}
```

From the MIDL above, we can infer that during version 1 of the **UniversalApiContract** API contract the **Block** class contained only these members.

- the **Block** constructor,
- the static **LineHeightProperty**, **LineStackingStrategyProperty**, **MarginProperty**, and **TextAlignmentProperty** dependency properties,
- the instance **LineHeight**, **LineStackingStrategy**, **Margin**, and **TextAlignment** properties.

But you can add members to the class in later versions. To specify when they were introduced, you apply a higher version `contract` attribute to just those members. So, the **Block** class in the example above added the following members during version 5 of the **UniversalApiContract**.

- the static **HorizontalTextAlignmentProperty** dependency property, and
- the instance **HorizontalTestAlignment** property.

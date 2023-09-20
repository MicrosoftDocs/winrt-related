---
description: A marker template that prevents an interface from being reported by IInspectable::GetIids.
title: winrt::cloaked marker struct template (C++/WinRT)
dev_langs: ["C++"]
ms.date: 09/20/2023
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, implement, interface
ms.workload: ["cplusplus"]
---

# winrt::cloaked marker struct template (C++/WinRT)

A marker template used to indicate to the [winrt::implements struct template](implements.md) that an implemented interface should not be included in the list of interfaces returned by the [IInspectable::GetIids](/windows/win32/api/inspectable/nf-inspectable-iinspectable-getiids) method (that is, the implemented interface should be "cloaked").

## Syntax
```cppwinrt
template<typename T>
struct cloaked;
```

## Remarks

By default, the implementation of **IInspectable::GetIids** reports all interfaces that derive from **IInspectable**. Use the **cloaked** marker template to indicate that a specific interface should be removed from that list.

## Examples

This first example applies when you derive directly from [implements](implements.md).

```cppwinrt
struct MyImplementation : implementation<MyImplementation, IFrameworkViewSource, cloaked<IStringable>>
{
    ...
};
```

This next example is for when you're authoring a runtime class.

```cppwinrt
struct BookSku : BookSkuT<BookSku, cloaked<IStringable>>
{
    ...
};
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)

---
description: A helper function template that determines whether or not the provided GUID is that of one of the specified runtime classes, coclasses, or interfaces.
title: winrt::is_guid_of function template (C++/WinRT)
dev_langs: ["C++"]
ms.date: 05/06/2021
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, is_guid_of
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::is_guid_of function template (C++/WinRT)

A helper function template that determines whether or not the provided GUID is that of one of the specified runtime classes, coclasses, or interfaces.

You can provide your own specialization(s) of **winrt::is_guid_of**. For more details, and code examples, see [Implement a COM interface that derives from another](/windows/uwp/cpp-and-winrt-apis/author-coclasses#implement-a-com-interface-that-derives-from-another).

## Syntax

```cppwinrt
template <typename... T>
bool is_guid_of(winrt::guid const& id) noexcept;
```

### Template parameters

`typename... T`
A variadic template parameter pack containing the types of the runtime classes, coclasses, or interfaces whose GUIDs you wish to match against the provided one.

### Parameters

`id`
A [winrt::guid](/uwp/cpp-ref-for-winrt/guid) function object of type `F`.

### Return value
`true` if *id* matches the GUID of one of the types *T*; otherwise, `false`.

## Requirements

**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 

* [winrt namespace](./winrt.md)
* [Author COM components with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-coclasses)

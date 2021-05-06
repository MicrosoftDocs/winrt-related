---

description: A helper function template that retrieves the GUID of a runtime class, coclass, or interface.
title: winrt::guid_of function template (C++/WinRT)
dev_langs: ["C++"]

ms.date: 03/15/2019
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, GUID
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::guid_of function template (C++/WinRT)

A helper function template that retrieves the GUID of a runtime class, coclass, or interface.

## Syntax
```cppwinrt
template <typename T>
constexpr winrt::guid const& guid_of() noexcept;
```

### Template parameters

`typename T`
The type of the runtime class, coclass, or interface whose GUID you wish to retrieve.

### Return value 

A **winrt::guid** value containing the globally unique identifier of `T`.

## Requirements

**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace (C++/WinRT)](winrt.md)

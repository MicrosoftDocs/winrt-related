---

description: A helper function template that retrieves the GUID of a runtime class, coclass, or interface.
title: winrt::guid_of function template (C++/WinRT)
dev_langs: ["C++"]

ms.date: 03/15/2019
ms.topic: reference
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, GUID
ms.workload: ["cplusplus"]
---

# winrt::guid_of function template (C++/WinRT)

A helper function template that retrieves the GUID of a runtime class, coclass, or interface; that is, the identifier of the WinRT type. For COM and WinRT interfaces, that's the identifier of the interface. For WinRT classes, it's the identifier of the default interface of the class.

It's only if and when `guid_v` (see the function's implementation) isn't specialized that the function falls back to using `__uuidof`, where applicable.

## Syntax
```cppwinrt
template <typename T>
constexpr winrt::guid const& guid_of() noexcept;
```

### Template parameters

`typename T`
The type of the runtime class, coclass, or interface whose GUID you wish to retrieve.

### Return value 

A [winrt::guid](./guid.md) value containing the globally unique identifier of `T`.

## Requirements

**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace (C++/WinRT)](winrt.md)

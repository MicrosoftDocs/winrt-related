---

description: A helper function which, given an object of a projected type, retrieves a pointer to the implementation.
title: winrt::get_self function template (C++/WinRT)
dev_langs: ["C++"]

ms.date: 08/29/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, projected, implementation, type
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::get_self function template (C++/WinRT)

A helper function which, given an object of a projected type, retrieves a pointer to the implementation. For more details, and code examples, see [Instantiating and returning implementation types and interfaces](/windows/uwp/cpp-and-winrt-apis/author-apis#instantiating-and-returning-implementation-types-and-interfaces).

## Syntax
```cppwinrt
template <typename D, typename I>
D* get_self(I const& from) noexcept
```

### Template parameters
`typename D`
An implementation type.

`typename I`
A projected interface type.

### Parameters
`from`
An object of a projected type, a pointer to whose implementation to retrieve.

### Return value 
A pointer to the implementation object that implements the interface object.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17763.0 (Windows 10, version 1809)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::make_self function template](make-self.md)
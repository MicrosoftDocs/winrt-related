---
description: A function template that wraps (or *boxes*) a scalar or array value inside a reference class object so that it can be passed to a function that expects **IInspectable**.
title: winrt::box_value function template (C++/WinRT)
dev_langs: ["C++"]
ms.date: 04/10/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, box, boxing
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::box_value function template (C++/WinRT)

> [!NOTE]
> You can box not only scalar values, but also most kinds of arrays (with the exception of arrays of enumerations) by using the **winrt::box_value** function.

A function template that wraps (or *boxes*) a scalar or array value inside a reference class object so that it can be passed to a function that expects **IInspectable**. An overload of the function also exists for [**winrt::hstring**](hstring.md). For more details, and code examples, see [Boxing and unboxing values to IInspectable with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/boxing).

## Syntax
```cppwinrt
winrt::Windows::Foundation::IInspectable box_value(winrt::hstring const& value);

template <typename T, typename = std::enable_if_t<!std::is_convertible_v<T, winrt::hstring>>>
winrt::Windows::Foundation::IInspectable box_value(T const& value);
```

### Template parameters
`typename T`
A scalar or array type.

### Parameters
`value`
A scalar or array value to box.

### Return value 
A reference class object containing the boxed value.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\Windows.Foundation.h

## See also 
* [winrt namespace](winrt.md)
* [winrt::unbox_value function template](unbox-value.md)
* [winrt::unbox_value_or function template](unbox-value-or.md)
* [Boxing and unboxing values to IInspectable with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/boxing)

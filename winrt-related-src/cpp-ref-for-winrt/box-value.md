---
author: stevewhims
description: A function template that wraps (or *boxes*) a scalar value inside a reference class object so that it can be passed to a function that expects **IInspectable**.
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 04/10/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, box, boxing
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::box_value function template ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A function template that wraps (or *boxes*) a scalar value inside a reference class object so that it can be passed to a function that expects **IInspectable**. An overload of the function also exists for [**winrt::hstring**](hstring.md). For more details, and code examples, see [Boxing and unboxing scalar values to IInspectable with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/boxing).

## Syntax
```cppwinrt
winrt::Windows::Foundation::IInspectable box_value(winrt::param::hstring const& value)

template <typename T, typename = std::enable_if_t<!std::is_convertible_v<T, winrt::param::hstring>>>
winrt::Windows::Foundation::IInspectable box_value(T const& value)
```

### Template parameters
`typename T`
A scalar type.

### Parameters
`value`
A scalar value to box.

### Return value 
A reference class object containing the boxed value.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17133.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::unbox_value function template](unbox-value.md)
* [winrt::unbox_value_or function template](unbox-value-or.md)
* [Boxing and unboxing scalar values to IInspectable with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/boxing)

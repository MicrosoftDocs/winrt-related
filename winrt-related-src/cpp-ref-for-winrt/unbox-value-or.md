---

title: winrt::unbox_value_or function template (C++/WinRT)
description: A function template that unwraps (or *unboxes*) a scalar value from inside a reference class object, with a fallback value, so that it can be processed in a function that expects **IInspectable**.
dev_langs: ["C++"]

ms.date: 04/10/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, box, boxing, unbox, unboxing
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::unbox_value_or function template (C++/WinRT)

> [!NOTE]
> You can unbox only scalar values (not arrays) by using the **winrt::unbox_value_or** function.

A function template that unwraps (or *unboxes*) a scalar value from inside a reference class object, with a fallback value, so that it can be processed in a function that expects **IInspectable**. An overload of the function also exists for [**winrt::hstring**](hstring.md). For more details, and code examples, see [Boxing and unboxing values to IInspectable with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/boxing).

## Syntax
```cppwinrt
template <typename T>
hstring unbox_value_or(winrt::Windows::Foundation::IInspectable const& value, winrt::hstring const& default_value);

template <typename T, typename = std::enable_if_t<!std::is_same_v<T, winrt::hstring>>>
T unbox_value_or(winrt::Windows::Foundation::IInspectable const& value, T const& default_value);
```

### Template parameters
`typename T`
A scalar type.

### Parameters
`default_value`
A fallback value to use should coercing the reference class object to the specified value type not be possible.

`value`
A reference class object containing a boxed value.

### Return value 
The scalar value contained inside the reference class object, or *default_value* if unboxing to the specified value type is not possible.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\Windows.Foundation.h

## See also 
* [winrt namespace](winrt.md)
* [winrt::box_value function template](box-value.md)
* [winrt::unbox_value function template](unbox-value.md)
* [Boxing and unboxing values to IInspectable with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/boxing)

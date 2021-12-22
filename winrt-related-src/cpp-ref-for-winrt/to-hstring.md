---

description: A helper function that converts an input value to a winrt::hstring containing the value's string representation.
title: winrt::to_hstring function (C++/WinRT)
dev_langs: ["C++"]

ms.date: 05/21/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.workload: ["cplusplus"]
---

# winrt::to_hstring function (C++/WinRT)

A helper function that converts an input value to a **winrt::hstring** containing the value's string representation. For more info, and a code example, see [winrt::hstring functions and operators](/windows/uwp/cpp-and-winrt-apis/strings#winrthstring-functions-and-operators).

## Syntax
```cppwinrt
inline winrt::hstring to_hstring(bool value);
inline winrt::hstring to_hstring(char16_t value);
inline winrt::hstring to_hstring(double value);
inline winrt::hstring to_hstring(float value);
inline winrt::hstring to_hstring(GUID const& value);
inline winrt::hstring to_hstring(winrt::hstring const& value) noexcept;
inline winrt::hstring to_hstring(int16_t value);
inline winrt::hstring to_hstring(int32_t value);
inline winrt::hstring to_hstring(int64_t value);
inline winrt::hstring to_hstring(int8_t value);
template <typename T> winrt::hstring to_hstring(T const& value);
inline winrt::hstring to_hstring(uint16_t value);
inline winrt::hstring to_hstring(uint32_t value);
inline winrt::hstring to_hstring(uint64_t value);
inline winrt::hstring to_hstring(uint8_t value);
```

## Parameters
`value`
The value to convert into a new **hstring** object.

### Return value
A new **hstring** object resulting from converting the parameter.

### Remarks
For the function template, specializations are generated only for types convertible from **std::basic_string_view**.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::to_string function](to-string.md)
* [String handling in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/strings)

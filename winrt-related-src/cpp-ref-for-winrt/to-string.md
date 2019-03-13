---
author: stevewhims
description: A helper function that converts a wide string to a std::string containing a UTF-8 narrow string.
title: winrt::to_string function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 05/21/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::to_string function (C++/WinRT)

A helper function that converts an input wide string to a **std::string** containing a UTF-8 narrow string by calling [**WideCharToMultiByte**](https://msdn.microsoft.com/library/windows/desktop/dd374130). For more info, and a code example, see [winrt::hstring functions and operators](/windows/uwp/cpp-and-winrt-apis/strings#winrthstring-functions-and-operators).

## Syntax
```cppwinrt
inline std::string to_string(std::wstring_view value);
```

### Parameters
`value`
A **std::wstring_view** value, or any value of a type convertible to **std::wstring_view**, to convert into a UTF-8 narrow string. This can be a [**winrt::hstring**](hstring.md), thanks to **hstring**'s [conversion operator to **std::wstring_view**](/uwp/cpp-ref-for-winrt/hstring#hstringoperator-stdwstringview).

### Return value
A **std::string** containing a UTF-8 narrow string resulting from converting the parameter.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::to_hstring function](to-hstring.md)
* [String handling in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/strings)
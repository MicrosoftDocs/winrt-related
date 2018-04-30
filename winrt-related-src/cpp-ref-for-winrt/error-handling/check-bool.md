---
author: stevewhims
description: A helper function that checks whether a value is false and, if so, retrieves the calling thread's last-error code value, and throws an exception using a C++/WinRT object that represents that error code.
title: winrt::check_bool function template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "jillfra"
ms.date: 04/30/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, check, throw, exception, bool, HRESULT, error, code
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::check_bool function template ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A helper function that checks whether a value is false and, if so, calls the [winrt::throw_last_error](throw-last-error.md) function to retrieve the calling thread's last-error code value, and throw an exception using a C++/WinRT object that represents that error code. Also see [winrt::hresult_error](hresult-error.md).

## Syntax
```cppwinrt
template<typename T>
void check_bool(T result);
```

### Template parameters
`typename T`
A type that's convertible to **bool**.

### Parameters
`result`
A value that's convertible to `false` (an error condition), or `true` (a success condition). An exception is thrown only if `result` is `false`.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](../winrt.md)
* [winrt::throw_hresult function](throw-hresult.md)
* [winrt::throw_last_error struct](throw-last-error.md)

---
author: stevewhims
description: A helper function that checks whether a code represents an error and, if so, maps the system error code of the value to an HRESULT value and throws an exception using a C++/WinRT object that represents the error code.
title: winrt::check_win32 function template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/30/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, check, throw, exception, system, HRESULT, error, code
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::check_win32 function template (C++/WinRT)
A helper function that checks whether a code represents an error and, if so, maps the system error code of the value to an HRESULT value and calls the [winrt::throw_hresult](throw-hresult.md) function to throw an exception that represents the error code. Also see [winrt::hresult_error](hresult-error.md).

## Syntax
```cppwinrt
template<typename T>
void check_win32(T result);
```

### Template parameters
`typename T`
An integer type.

### Parameters
`result`
A code, which may be a success code or an error code. An exception is thrown only if `result` is an error code.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](../winrt.md)
* [winrt::hresult_error struct](hresult-error.md)
* [winrt::throw_hresult function](throw-hresult.md)
* [Error handling with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/error-handling)

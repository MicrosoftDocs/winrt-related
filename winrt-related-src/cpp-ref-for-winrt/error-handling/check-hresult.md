---
author: stevewhims
description: A helper function that checks whether an HRESULT code represents an error and, if so, throws an exception using a C++/WinRT object that represents the error code.
title: winrt::check_hresult function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/30/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, check, throw, exception, hresult_error, HRESULT, error, code
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::check_hresult function ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A helper function that checks whether an HRESULT code represents an error and, if so, calls the [winrt::throw_hresult](throw-hresult.md) function to throw an exception that represents the error code. Also see [winrt::hresult_error](hresult-error.md).

## Syntax
```cppwinrt
__forceinline void check_hresult(HRESULT const result);
```

### Parameters
`result`
An HRESULT code, which may be a success code or an error code. An exception is thrown only if `result` is an error code.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](../winrt.md)
* [winrt::hresult_error struct](hresult-error.md)
* [winrt::throw_hresult function](throw-hresult.md)
* [Error handling with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/error-handling)

---
author: stevewhims
description: A helper function that retrieves the calling thread's last-error code value, and throws an exception using a C++/WinRT object that represents that error code.
title: winrt::throw_last_error function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/30/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, last-error, throw, exception, hresult_error, HRESULT, error, code
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::throw_last_error function ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A helper function that calls [GetLastError](https://msdn.microsoft.com/library/windows/desktop/ms679360) to retrieve the calling thread's last-error code value, then calls the [winrt::throw_hresult](throw-hresult.md) function to throw an exception that represents that error code. Also see [winrt::hresult_error](hresult-error.md).

## Syntax
```cppwinrt
[[noreturn]] inline void throw_last_error();
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](../winrt.md)
* [winrt::hresult_error struct](hresult-error.md)
* [winrt::throw_hresult function](throw-hresult.md)
* [Error handling with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/error-handling)

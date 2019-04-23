---
author: stevewhims
description: A helper function that takes a HRESULT error code, and throws an exception using a C++/WinRT object that represents that error code.
title: winrt::throw_hresult function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/26/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, throw, exception, hresult_error, HRESULT, error, code
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::throw_hresult function (C++/WinRT)
A helper function that takes a HRESULT error code, and throws an exception using a [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt) object (or a standard object) that represents that error code.

If the error code is E_OUTOFMEMORY, then **std::bad_alloc** is thrown. If the error code is a common HRESULT error code, then one of the specialized types derived from [winrt::hresult_error](hresult-error.md) is thrown. For example, E_INVALIDARG causes a [winrt::hresult_invalid_argument](hresult-invalid-argument.md) to be thrown. Otherwise, **winrt::hresult_error** is thrown.

## Syntax
```cppwinrt
[[noreturn]] inline __declspec(noinline) void throw_hresult(HRESULT const result);
```

### Parameters
`result`
An HRESULT code that represents the error that was encountered.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](../winrt.md)
* [winrt::hresult_error struct](hresult-error.md)
* [Error handling with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/error-handling)

---

description: A helper function, for use in a catch block, that turns the last exception thrown into a HRESULT error code.
title: winrt::to_hresult function (C++/WinRT)
dev_langs: ["C++"]

ms.date: 04/30/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, check, throw, catch, exception, HRESULT, error, code
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::to_hresult function (C++/WinRT)
A helper function, for use in a catch block, that turns the last exception thrown into a HRESULT error code. In a catch block that catches [winrt::hresult_error](hresult-error.md), you can get an HRESULT directly from that type by using the [hresult_error::to_abi](./hresult-error.md#hresult_errorto_abi-function) member function. In other catch blocks, you can call the **winrt::to_hresult** function to get a HRESULT, if the exception that was thrown is any of: **winrt::hresult_error**, **std::bad_alloc**, **std::out_of_range**, **std::invalid_argument**, or **std::exception**.

**to_hresult** is a low-level function that you'll seldom need to use.

## Syntax
```cppwinrt
inline __declspec(noinline) HRESULT to_hresult() noexcept;
```

### Return value
The HRESULT error code represented by the last exception thrown.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](../winrt.md)
* [winrt::hresult_error struct](hresult-error.md)
* [Error handling with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/error-handling)
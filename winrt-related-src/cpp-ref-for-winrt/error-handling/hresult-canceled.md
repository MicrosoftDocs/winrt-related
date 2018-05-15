---
author: stevewhims
description: A type derived from winrt::hresult_error, representing an ERROR_CANCELLED HRESULT error code.
title: winrt::hresult_canceled struct (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/25/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, hresult, error, code, ERROR_CANCELLED
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::hresult_canceled struct ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A type derived from **winrt::hresult_error**, representing an ERROR_CANCELLED HRESULT error code. Also see the [winrt::hresult_error](hresult-error.md) topic to learn about the members that are also available to **winrt::hresult_canceled**.

## Syntax
```cppwinrt
struct hresult_canceled : winrt::hresult_error
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Constructors
|Constructor|Description|
|------------|-----------------|
|[hresult_canceled::hresult_canceled constructor](#hresultcanceledhresultcanceled-constructor)|Initializes a new instance of the **hresult_canceled** struct with a copy of the input data.|

## hresult_canceled::hresult_canceled constructor
Initializes a new instance of the **hresult_canceled** struct with a copy of the input data.

### Syntax
```cppwinrt
hresult_canceled() noexcept;
hresult_canceled(winrt::hstring const& message) noexcept;
hresult_canceled(winrt::hresult_error::from_abi_t) noexcept
```

### Parameters
`message`
An informative string to help developers to correct the reported error condition.

## See also 
* [winrt namespace](../winrt.md)
* [winrt::hresult_error struct](hresult-error.md)
* [Error handling with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/error-handling)

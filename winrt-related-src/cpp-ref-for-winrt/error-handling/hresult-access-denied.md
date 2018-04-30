---
author: stevewhims
description: A type derived from winrt::hresult_error, representing an E_ACCESSDENIED HRESULT error code.
title: winrt::hresult_access_denied struct (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "jillfra"
ms.date: 04/25/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, hresult, error, code, E_ACCESSDENIED
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::hresult_access_denied struct ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A type derived from **winrt::hresult_error**, representing an E_ACCESSDENIED HRESULT error code. Also see the [winrt::hresult_error](hresult-error.md) topic to learn about the members that are also available to **winrt::hresult_access_denied**.

## Syntax
```cppwinrt
struct hresult_access_denied : winrt::hresult_error
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Constructors
|Constructor|Description|
|------------|-----------------|
|[hresult_access_denied::hresult_access_denied constructor](#hresultaccessdeniedhresultaccessdenied-constructor)|Initializes a new instance of the **hresult_access_denied** struct with a copy of the input data.|

## hresult_access_denied::hresult_access_denied constructor
Initializes a new instance of the **hresult_access_denied** struct with a copy of the input data.

### Syntax
```cppwinrt
hresult_access_denied() noexcept;
hresult_access_denied(winrt::hstring const& message) noexcept;
hresult_access_denied(winrt::hresult_error::from_abi_t) noexcept
```

### Parameters
`message`
An informative string to help developers to correct the reported error condition.

## See also 
* [winrt namespace](../winrt.md)
* [winrt::hresult_error struct](hresult-error.md)

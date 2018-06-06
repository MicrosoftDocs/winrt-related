---
author: stevewhims
description: A type containing static helper functions for converting a Windows::Foundation::DateTime (that is, a std::chrono::time_point) to and from FILETIME, and to and from time_t.
title: winrt::clock struct (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/10/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, weak
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::clock struct ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A type containing static helper functions for converting a [Windows::Foundation::DateTime](/uwp/api/windows.foundation.datetime) (that is, a [std::chrono::time_point](/cpp/standard-library/time-point-class)) to and from [FILETIME](https://msdn.microsoft.com/library/windows/desktop/ms724284), and to and from [time_t](/cpp/c-runtime-library/reference/time-time32-time64).

## Syntax
```cppwinrt
struct clock
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member functions
|Function|Description|
|------------|-----------------|
|[clock::now function](#clocknow-function)|Retrieves the current time as a **Windows::Foundation::DateTime**.|
|[clock::from_FILETIME function](#clockfromfiletime-function)|Converts a **FILETIME** value to a **Windows::Foundation::DateTime**.|
|[clock::from_time_t function](#clockfromtimet-function)|Converts a **time_t** value to a **Windows::Foundation::DateTime**.|
|[clock::to_FILETIME function](#clocktofiletime-function)|Converts a **Windows::Foundation::DateTime** value to a **FILETIME**.|
|[clock::to_time_t function](#clocktotimet-function)|Converts a **Windows::Foundation::DateTime** value to a **time_t**.|

## clock::now function
Retrieves the current time as a **Windows::Foundation::DateTime**.

### Syntax
```cppwinrt
static Windows::Foundation::DateTime now() noexcept;
```

### Return value 
The current time as a **Windows::Foundation::DateTime**.

## clock::from_FILETIME function
Converts a **FILETIME** value to a **Windows::Foundation::DateTime**.

### Syntax
```cppwinrt
static Windows::Foundation::DateTime from_FILETIME(FILETIME const& time) noexcept;
```

### Parameters
`time`
A **FILETIME** value to convert to a **Windows::Foundation::DateTime**.

### Return value 
The **FILETIME** value converted into a **Windows::Foundation::DateTime**.

## clock::from_time_t function
Converts a **time_t** value to a **Windows::Foundation::DateTime**.

### Syntax
```cppwinrt
static Windows::Foundation::DateTime from_time_t(time_t time) noexcept;
```

### Parameters
`time`
A **time_t** value to convert to a **Windows::Foundation::DateTime**.

### Return value 
The **time_t** value converted into a **Windows::Foundation::DateTime**.

## clock::to_FILETIME function
Converts a **Windows::Foundation::DateTime** value to a **FILETIME**.

### Syntax
```cppwinrt
static FILETIME to_FILETIME(Windows::Foundation::DateTime const& time) noexcept;
```

### Parameters
`time`
A **Windows::Foundation::DateTime** value to convert to a **FILETIME**.

### Return value 
The **Windows::Foundation::DateTime** value converted into a **FILETIME**.

## clock::to_time_t function
Converts a **Windows::Foundation::DateTime** value to a **time_t**.

### Syntax
```cppwinrt
static time_t to_time_t(Windows::Foundation::DateTime const& time) noexcept;
```

### Parameters
`time`
A **Windows::Foundation::DateTime** value to convert to a **time_t***.

### Return value 
The **Windows::Foundation::DateTime** value converted into a **time_t**.

## See also 
* [winrt namespace](winrt.md)
* [FILETIME](https://msdn.microsoft.com/library/windows/desktop/ms724284)
* [std::chrono::time_point](/cpp/standard-library/time-point-class)
* [time_t](/cpp/c-runtime-library/reference/time-time32-time64)
* [Windows::Foundation::DateTime](/uwp/api/windows.foundation.datetime)

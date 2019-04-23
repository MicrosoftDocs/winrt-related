---
author: stevewhims
description: A helper function that retrieves the trust level of a C++/WinRT object.
title: winrt::get_trust_level function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 05/01/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, trust, level, IInspectable, GetTrustLevel
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::get_trust_level function (C++/WinRT)
A helper function that retrieves the trust level of a [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt) object. This is the same value returned from a call to [**IInspectable::GetTrustLevel**](https://msdn.microsoft.com/library/br205824).

## Syntax
```cppwinrt
inline winrt::Windows::Foundation::TrustLevel get_trust_level(winrt::Windows::Foundation::IInspectable const& object);
```

### Parameters
`object`
A C++/WinRT object to operate on.

### Return value 
The trust level of the object, in the form of a value of the [**TrustLevel enumeration**](https://msdn.microsoft.com/library/br224625).

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace (C++/WinRT)](winrt.md)
* [winrt::com_array struct template](com-ptr.md)
* [IInspectable::GetTrustLevel](https://msdn.microsoft.com/library/br205824)
* [TrustLevel enumeration](https://msdn.microsoft.com/library/br224625)

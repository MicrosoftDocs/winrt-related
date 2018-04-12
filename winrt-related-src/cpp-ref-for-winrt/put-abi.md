---
author: stevewhims
description: A helper function that retrieves the address of a C++/WinRT object's underlying IUnknown interface pointer so that it can be set to another value.
title: winrt::put_abi function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 04/10/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, IUnknown
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::put_abi function (C++/WinRT)
A helper function that retrieves the address of a C++/WinRT object's underlying [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) pointer so that it can be set to another value.

## Syntax
```cppwinrt
template <typename T, typename = std::enable_if_t<!std::is_base_of_v<winrt::Windows::Foundation::IUnknown, T>>>
auto put_abi(T& object) noexcept

inline void** put_abi(winrt::Windows::Foundation::IUnknown& object) noexcept

inline HSTRING* put_abi(winrt::hstring& object) noexcept

template<typename T>
auto put_abi(winrt::com_array<T>& object) noexcept

template <typename T>
auto put_abi(winrt::com_ptr<T>& object) noexcept

template <typename T>
auto put_abi(winrt::weak_ref<T>& object) noexcept
```

### Parameters
`object`
The C++/WinRT object the address of whose **IUnknown** interface pointer to retrieve.

### Return value 
The address of the **IUnknown** interface pointer of the C++/WinRT object.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17133.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::get_abi function](get-abi.md)

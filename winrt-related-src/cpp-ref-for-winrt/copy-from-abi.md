---
author: stevewhims
description: A helper function that copies to a C++/WinRT object from a handle, or from a raw pointer.
title: winrt::copy_from_abi function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "jillfra"
ms.date: 04/11/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, copy_from_abi
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::copy_from_abi function ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A helper function that copies to a C++/WinRT object from a handle, or from a raw pointer. Clears the C++/WinRT object, or decrements the reference count on any currently referenced interface, copies the parameter, and begins managing the handle or interface pointed to by it.

## Syntax
```cppwinrt
template <typename T, typename V, typename = std::enable_if_t<!std::is_base_of_v<winrt::Windows::Foundation::IUnknown, T>>>
void copy_from_abi(T& object, V&& value);

void copy_from_abi(winrt::hstring& object, HSTRING value);

void copy_from_abi(winrt::Windows::Foundation::IUnknown& object, void* value) noexcept;
```

### Parameters
`object`
A C++/WinRT object to operate on.

`value`
A handle, or a raw pointer to a target whose lifetime should be managed by the C++/WinRT object.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::com_ptr struct template](com-ptr.md)
* [winrt::hstring struct](hstring.md)
* [Windows::Foundation::IUnknown struct](windows-foundation-iunknown.md)

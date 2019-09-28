---
author: stevewhims
description: A helper function that attaches a C++/WinRT object to a handle, or to a raw pointer that owns a reference to its target.
title: winrt::attach_abi function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/11/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, attach_abi
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::attach_abi function (C++/WinRT)
A helper function that attaches a [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt) object to a handle, or to a raw pointer that owns a reference to its target. In the case of pointers, an additional reference is not added. If needed, you can use this function to coalesce references. For more info, and code examples, see [Interop between C++/WinRT and the ABI](/windows/uwp/cpp-and-winrt-apis/interop-winrt-abi).


## Syntax
```cppwinrt
template <typename T>
void attach_abi(com_ptr<T>& object, winrt::impl::abi_t<T>* value) noexcept;

void attach_abi(winrt::hstring& object, void* value) noexcept;

void attach_abi(winrt::Windows::Foundation::IUnknown& object, void* value) noexcept;
```

### Parameters
`object`
A C++/WinRT object to operate on.

`value`
A handle, or a raw pointer that owns a reference to its target.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::com_ptr struct template](com-ptr.md)
* [winrt::hstring struct](hstring.md)
* [winrt::Windows::Foundation::IUnknown struct](windows-foundation-iunknown.md)
* [Interop between C++/WinRT and the ABI](/windows/uwp/cpp-and-winrt-apis/interop-winrt-abi)

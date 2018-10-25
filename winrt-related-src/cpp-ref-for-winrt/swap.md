---
author: stevewhims
description: A helper function that swaps the contents of two values.
title: winrt::swap function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/11/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, swap
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::swap function (C++/WinRT)

A helper function that swaps the contents of two values.

## Syntax
```cppwinrt
void swap(winrt::com_array& left, winrt::com_array& right) noexcept;
void swap(winrt::com_ptr& left, winrt::com_ptr& right) noexcept;
void swap(winrt::handle_type& left, winrt::handle_type& right) noexcept;
void swap(winrt::hstring& left, winrt::hstring& right) noexcept;
void swap(winrt::Windows::Foundation::IUnknown& left, winrt::Windows::Foundation::IUnknown& right) noexcept;
```

### Parameters
`left` `right`
A value to mutually swap with that of the other parameter. For example, if the values represent pointers, then their contents are swapped so that they point at one another's target.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::com_array struct template](com-array.md)
* [winrt::com_ptr struct template](com-ptr.md)
* [winrt::hstring struct](hstring.md)
* [winrt::Windows::Foundation::IUnknown struct](windows-foundation-iunknown.md)

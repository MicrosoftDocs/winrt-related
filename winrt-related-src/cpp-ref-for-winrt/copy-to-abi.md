---

description: A helper function that copies to a handle, or to a pointer, from a C++/WinRT object.
title: winrt::copy_to_abi function (C++/WinRT)
dev_langs: ["C++"]

ms.date: 04/11/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, copy_to_abi
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::copy_to_abi function (C++/WinRT)
A helper function that copies to a handle, or to a pointer, from a [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt) object. Increments the reference count on any currently referenced interface, and copies that interface's memory address into the parameter (incrementing any reference count on the parameter). This function lets you hand out a reference to the same interface without calling [QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)). For more info, and code examples, see [Interop between C++/WinRT and the ABI](/windows/uwp/cpp-and-winrt-apis/interop-winrt-abi).

## Syntax
```cppwinrt
template <typename T, typename V, typename =
std::enable_if_t<!std::is_base_of_v<winrt::Windows::Foundation::IUnknown, T>>>
void copy_to_abi(T const& object, V& value);

void copy_to_abi(hstring const& object, void*& value);

void copy_to_abi(winrt::Windows::Foundation::IUnknown const& object, void*& value) noexcept;
```

### Parameters
`object`
A C++/WinRT object to operate on.

`value`
A handle reference, or a raw pointer reference; via which to copy the pointer to the C++/WinRT object's handle or target. In the case of the `IUnknown const&, void*&` overload, the function calls **AddRef** on *value*.

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

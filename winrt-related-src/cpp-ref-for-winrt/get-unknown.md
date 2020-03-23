---

description: A helper function that returns the address of the underlying raw [IUnknown interface](/windows/win32/api/unknwn/nn-unknwn-iunknown) of an object of a projected type.
title: winrt::get_unknown function (C++/WinRT)
dev_langs: ["C++"]
ms.date: 03/17/2020
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, IUnknown
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::get_unknown function (C++/WinRT)

A helper function that returns the address of (in other words, a pointer to) the underlying raw [IUnknown interface](/windows/win32/api/unknwn/nn-unknwn-iunknown) of an object of a projected type (for info about *projected types*, see [Consume APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/consume-apis)).

This function helps you call methods (such as COM methods) that expect a pointer to [::IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown). See the [**Example**](#example) section in this topic for more details. Also see the [winrt::Windows::Foundation::IUnknown struct](/uwp/cpp-ref-for-winrt/windows-foundation-iunknown#get_unknown-function).

It's a good idea to `#include <unknwn.h>` explicity whenever you use **winrt::get_unknown**, even if that header has been included by another header.

## Syntax
```cppwinrt
inline ::IUnknown* get_unknown(winrt::Windows::Foundation::IUnknown const& object) noexcept;
```

### Parameters
`object`
An object of a projected type to operate on (or any [winrt::Windows::Foundation::IUnknown](/uwp/cpp-ref-for-winrt/windows-foundation-iunknown#get_unknown-function) value).

### Return value 
The address of the underlying raw [IUnknown interface](/windows/win32/api/unknwn/nn-unknwn-iunknown) as a pointer to **IUnknown**.

### Example

```cppwinrt
#include <dxgi1_2.h>
#include <d3d12.h>
#include <unknwn.h>
#include <winrt/Windows.UI.Core.h>
...
winrt::com_ptr<::IDXGIFactory2> factory;
winrt::com_ptr<::ID3D12CommandQueue> commandQueue;
winrt::Windows::UI::Core::CoreWindow coreWindow{ nullptr };
DXGI_SWAP_CHAIN_DESC1 swapChainDesc{};
winrt::com_ptr<::IDXGISwapChain1> swapChain;

// Initialize the variables here.

winrt::check_hresult(
    factory->CreateSwapChainForCoreWindow(
        commandQueue.get(),
        winrt::get_unknown(coreWindow),
        &swapChainDesc,
        nullptr,
        swapChain.put())
);
```

The **get_unknown** function is not intended for cases where you're authoring a type that *does* implement a COM interface, but that *doesn't* implement a Windows Runtime type. In a case like that, you can pass a pointer to your type wherever [::IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) is expected, as shown below.

```cppwinrt
HRESULT FunctionThatExpectsAnIUnknown(::IUnknown * pUnk);
...
struct MyRuntimeClass : winrt::implements<MyRuntimeClass, IMyCOMInterface>
{
    ...

    HRESULT MyRuntimeClass::MemberFunction()
    {
        return FunctionThatExpectsAnIUnknown(this);
    }
}
```

For more info, see [Author APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-apis).

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [IUnknown interface](/windows/win32/api/unknwn/nn-unknwn-iunknown)
* [winrt::Windows::Foundation::IUnknown struct](/uwp/cpp-ref-for-winrt/windows-foundation-iunknown#get_unknown-function)
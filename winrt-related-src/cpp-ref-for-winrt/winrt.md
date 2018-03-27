---
author: stevewhims
description: API reference content for the winrt namespace from C++/WinRT.
title: winrt namespace (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 03/01/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt namespace (C++/WinRT)
> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

The **winrt** namespace provides custom data types belonging to [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/index)&mdash;the standard, modern C++17 language projection for Windows Runtime (WinRT) APIs. These custom types provide appropriate conversions to and from standard types so that, much of the time, you can continue to use the standard C++ language features that you're accustomed to using, and the source code that you already have.

Also provided in the **winrt** namespace are functions (for creating runtime class instances, boxing and unboxing, etc.), smart pointers, and other facilities.

## Types
| Type | Description |
| - | - |
| [array_view struct template](array-view.md) | A view, or span, of a contiguous series of values. |
| [box_value function template](box-value.md) | A function template that wraps (or *boxes*) a scalar value inside a reference class object so that it can be passed to a function that expects **IInspectable**. |
| [com_array struct template](com-array.md) | A view, or span, of a contiguous series of values for passing to and from WinRT APIs. |
| [com_ptr struct template](com-ptr.md) | A reference-counted COM smart pointer template. |
| [get_abi function template](get-abi.md) | A helper function that retrieves a pointer to a C++/WinRT object's underlying [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) pointer. |
| [hstring struct](hstring.md) | A sequential collection of UTF-16 Unicode characters representing a text string. |
| [implements struct template](implements.md) | A base struct template that implements one or more Windows Runtime interfaces on behalf of a derived type. |
| [make function template](make.md) | A factory method that returns an instance of the projected type for a runtime class when parameterized with the corresponding implementation type. |
| [make_self function template](make-self.md) | A factory method that returns a [com_ptr](com-ptr.md) to an instance of the implementation type for a runtime class. |
| [unbox_value function template](unbox-value.md) | A function template that unwraps (or *unboxes*) a scalar value from inside a reference class object so that it can be processed in a function that expects **IInspectable**. |
| [unbox_value_or function template](unbox-value-or.md) | A function template that unwraps (or *unboxes*) a scalar value from inside a reference class object, with a fallback value, so that it can be processed in a function that expects **IInspectable**. |
| [xaml_typename function template](xaml-typename.md) | A helper function that returns the type name of a Windows Runtime type, in the form of a [Windows::UI::Xaml::Interop::TypeName](/uwp/api/windows.ui.xaml.interop.typename) object. |

## See also 
[C++/WinRT](/windows/uwp/cpp-and-winrt-apis/index)

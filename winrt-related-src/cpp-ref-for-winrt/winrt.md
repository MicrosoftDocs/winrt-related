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

The **winrt** namespace provides custom data types belonging to C++/WinRT&mdash;the [standard C++ language projection for Windows Runtime (WinRT) APIs](/windows/uwp/cpp-and-winrt-apis/index?branch=live). These custom types provide appropriate conversions to and from standard types so that, much of the time, you can continue to use the standard C++ language features that you're accustomed to using, and the source code that you already have.

## Types

| Type | Description |
| - | - |
| [array_view struct template](array-view.md) | A view, or span, of a contiguous series of values. |
| [com_array struct template](com-array.md) | A view, or span, of a contiguous series of values for passing to and from WinRT APIs. |
| [hstring struct](hstring.md) | A sequential collection of UTF-16 Unicode characters representing a text string. |
| [make function template](make.md) | A factory method that returns an instance of the projected type for a runtime class when parameterized with the corresponding implementation type. |

## See also 
[C++/WinRT](/windows/uwp/cpp-and-winrt-apis/index?branch=live)

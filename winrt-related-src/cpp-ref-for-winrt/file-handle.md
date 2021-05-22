---

description: Represents a Windows file handle object.
title: winrt::file_handle struct (C++/WinRT)
dev_langs: ["C++"]

ms.date: 05/14/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, Windows, file, handle
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::file_handle struct (C++/WinRT)
Represents a Windows file handle object. **winrt::file_handle** is a type alias for **winrt::handle_type&lt;winrt::file_handle_traits&gt;**, so see the [**winrt::handle_type**](handle-type.md) struct template topic to learn about the functions and operators that are available to **winrt::file_handle**.

## Syntax
```cppwinrt
struct file_handle_traits {};

using file_handle = handle_type<file_handle_traits>;
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::handle_type struct template](handle-type.md)
* [winrt::handle struct](handle.md)

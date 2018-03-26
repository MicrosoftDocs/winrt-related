---
author: stevewhims
description: A helper function that returns the type name of a Windows Runtime type in a Windows::UI::Xaml::Interop::TypeName object.
title: winrt::xaml_typename function template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 03/23/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, navigation, typename
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::xaml_typename function template (C++/WinRT)
> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

A helper function that returns the type name of a Windows Runtime type in a [Windows::UI::Xaml::Interop::TypeName](/uwp/api/windows.ui.xaml.interop.typename) object.

## Syntax
```cppwinrt
template <typename T>
inline Windows::UI::Xaml::Interop::TypeName xaml_typename()
```

### Template parameters
`typename T`
A Windows Runtime class type.

### Return value 
A [Windows::UI::Xaml::Interop::TypeName](/uwp/api/windows.ui.xaml.interop.typename) object representing the type.

### Example
```cppwinrt
// App.cpp
void App::OnLaunched(LaunchActivatedEventArgs const& e)
{
    Frame rootFrame{ nullptr };
    auto content = Window::Current().Content();
    if (content) rootFrame = content.try_as<Frame>();
    ...
    rootFrame.Navigate(xaml_typename<Bookstore::MainPage>(), box_value(e.Arguments()));
    ...
}
```

## Requirements
**Minimum supported SDK:** Windows SDK for Windows 10, version 1803

**Namespace:** winrt

**Header** %ProgramFiles(x86)%\Windows Kits\10\Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace (C++/WinRT)](winrt.md)

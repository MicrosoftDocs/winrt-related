---
title: Windows UI library
description: Lists toolkits for UWP app development. 
ms.author: mijacobs
author: mijacobs
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 07/09/2018
keywords: windows 10, uwp, toolkit sdk
---

# Windows UI Library (Preview edition)

The Windows UI Library is a set of NuGet packages that provide controls and other user interface elements for UWP apps. It also enables down-level compatibility with earlier versions of Windows 10, so your app works even if users don't have the latest OS. 

## Features
* New controls

    The Windows UI Library contains new controls that haven't yet shipped as part of the Windows platform. 

* Updated versions of existing controls

    The library also contains updated versions of existing controls that you can use with earlier versions of Windows 10. 

* Support for earlier versions of Windows 10

    Windows UI Library APIs work on earlier versions of Windows 10, so you don't have to include version checks or conditional XAML to support users who might not be running the very latest OS. 

* XamlDirect 

    XamlDirect enables you to use [XamlDirect APIs](/uwp/api/microsoft.ui.xaml.core.direct) on earlier versions of Windows 10 without needing to write special code to handle multiple target Windows 10 versions. 

    The Xaml Direct APIs, designed for middleware developers, gives you access to a lower-level Xaml features which provide better CPU and working set performance. 

## Approved for the Microsoft Store

The controls and features in the Windows UI Library are approved for the Microsoft Store, so go ahead and add them to your app! 

## Examples

The dev branch of the Xaml Controls Gallery sample app has also been updated to use WinUI as a usage example:
* [Xaml Controls Gallery sample app on GitHub (dev branch)](
https://github.com/Microsoft/Windows-universal-samples/tree/dev/Samples/XamlUIBasics)


## Documentation

How-to articles for Windows UI Library controls are located with the rest of our [UWP controls documentation](/windows/uwp/design/controls-and-patterns/). We have articles for most of the new controls, and more articles are on the way.

API reference docs are located here: [Windows UI Library APIs](/uwp/api/overview/winui/).

## Install and use the Windows UI Library 

For instructions, see [Getting started with the Windows UI Library](getting-started.md). 

## NuGet package list
The Windows UI Library contains multiple NuGet packages: [Windows UI Library NuGet package list](nuget-packages.md). 



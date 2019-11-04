---
title: WinUI 3.0 Alpha (November 2019)
description: Overview of the WinUI 3.0 Alpha.
author: jebishop
ms.author: kbridge
ms.date: 11/04/2019
ms.topic: reference
---

# WinUI 3.0 Alpha (November 2019)

WinUI 3.0 is a major update to the Windows 10 UI platform planned for release in 2020.

For more information on the roadmap and benefits of WinUI 3.0, see the [Windows UI Library Roadmap](https://github.com/microsoft/microsoft-ui-xaml/blob/master/docs/roadmap.md) on GitHub.

The WinUI 3.0 Alpha is a pre-release build of WinUI 3.0, and we welcome your feedback in the [WinUI GitHub repo](https://github.com/microsoft/microsoft-ui-xaml).

> [!NOTE]
> The WinUI 3.0 Alpha is intended for early evaluation and to gather feedback from the developer community. It should **NOT** be used for production apps.

## Try the WinUI 3.0 Alpha

To try the WinUI 3.0 Alpha, install the latest Visual Studio Preview then either start with a blank [Visual Studio project template](#visual-studio-project-templates), or clone and build the [XAML Controls Gallery (WinUI 3.0 Alpha) sample app](#xaml-controls-gallery-winui-30-alpha-branch).

### Set up Visual Studio

> [!IMPORTANT]
> Visual Studio 2019 Preview version 16.4 or newer is required for building apps using the WinUI 3.0 Alpha.

See [Visual Studio Preview](https://visualstudio.microsoft.com/vs/preview) to download the latest Visual Studio Preview.

You must include the following workloads when installing the Visual Studio Preview:

* .NET Desktop Development
* Universal Windows Platform development

To build C++ apps you must also include the following workloads:

* Desktop development with C++
* The *C++ (v142) Universal Windows Platform tools* optional component for the Universal Windows Platform workload

#### Additional steps for April 2018 update

If you are running the April 2018 Update (1803), you may need to manually install the Visual C redistributable for Visual Studio 2019.

> [!NOTE]
> This step is not required for newer versions of Windows 10.

https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads

### Visual Studio project templates

To access the WinUI 3.0 Alpha and project templates, fill out the following form:

**https://aka.ms/WinUI3AlphaAccess**

After completing the form, you must download a Visual Studio Extension (`.vsix`) to add the WinUI project templates to Visual Studio 2019.

For directions on how to add the `.vsix` to Visual Studio, see [Finding and Using Visual Studio Extensions](https://docs.microsoft.com/visualstudio/ide/finding-and-using-visual-studio-extensions?view=vs-2019#install-without-using-the-manage-extensions-dialog-box).

After installing the `.vsix` extension you can create a new WinUI 3.0 project by searching for "WinUI" and selecting one of the available C# or C++ templates.

![WinUI 3 Visual Studio Templates](images/WinUI3Templates.png)

### Visual Studio project configuration

> [!IMPORTANT]
> Your project’s Target version must be 18362 or higher and the Min version must be 17134 or higher to use the WinUI 3.0 Alpha.

> [!NOTE]
> If your Visual Studio solution platform is set to x86 then your app may fail to deploy on 64-bit versions of Windows. To work around this issue you can change your platform configuration to x64.

### Xaml Controls Gallery (WinUI 3.0 Alpha branch)

Check out the WinUI 3.0 Alpha branch of the Xaml Controls Gallery to see a working example of a WinUI 3 app including available controls and features.

https://github.com/microsoft/Xaml-Controls-Gallery/tree/winui3alpha

![WinUI 3 Xaml Controls Gallery](images/WinUI3XamlControlsGallery.png)

## Build apps

Aside from the limitations and known issues outlined below, building an app using the WinUI 3.0 Alpha is very similar to building a UWP app with Xaml and WinUI 2.x, so most of the guidance and documentation for UWP apps and `Windows.UI` APIs is applicable.

For more information on how to create a UWP app, see [Start coding](https://docs.microsoft.com/windows/uwp/get-started/create-uwp-apps).

The main difference is that WinUI 3 APIs are in the `Microsoft.UI` namespace instead of the `Windows.UI` namespace, so you may need to update namespaces when copying and pasting sample code. Similarly, libraries and components using UI controls from `Windows.UI.Xaml` are not compatible with WinUI 3 and must be updated to `Microsoft.UI.Xaml`.

## Alpha limitations and known issues

The Alpha build is incomplete, so you should expect some bugs and limitations.

The following items are some of the known issues with the WinUI 3.0 Alpha. If you find an issue that isn't listed below, please let us know by contributing to an existing issue or filing a new issue on the [WinUI GitHub repo](https://github.com/microsoft/microsoft-ui-xaml/issues).

### Project types

The WinUI 3.0 Alpha project templates for Visual Studio only support building C# and C++/WinRT components and apps using the UWP app model.

Future updates will add support for additional project types and languages, including .NET Core 3.1+ and the desktop (win32) app model.

### Platform and OS support

The WinUI 3 Alpha works on PCs running the Windows 10 April 2018 Update (1803) and newer.

Future updates will include support for a wider range of Windows versions and devices.

### Controls and features

The following list shows the UI controls and features that are not included (or not fully functional) in the first Alpha build.

* [AcrylicBrush](https://docs.microsoft.com/uwp/api/windows.ui.xaml.media.acrylicbrush)
* [ContentLink](https://docs.microsoft.com/uwp/api/windows.ui.xaml.documents.contentlink)
* [HandWritingView](https://docs.microsoft.com/uwp/api/windows.ui.xaml.controls.handwritingview)
* [InkCanvas](https://docs.microsoft.com/uwp/api/windows.ui.xaml.controls.inkcanvas), [InkToolbar](https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.InkToolbar) and related APIs 
* [MapControl](https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.Maps.MapControl)
* [MediaPlayerElement](https://docs.microsoft.com/uwp/api/windows.ui.xaml.controls.mediaplayerelement), [MediaElement](https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.MediaElement) and related APIs
* [RevealBrush](https://docs.microsoft.com/uwp/api/windows.ui.xaml.media.revealbrush)
* [SwapChainPanel](https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.SwapChainPanel) and [SwapChainBackgroundPanel](https://docs.microsoft.com/uwp/api/windows.ui.xaml.controls.swapchainbackgroundpanel)
* [System.ComponentModel.INotifyPropertyChanged](https://docs.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged?view=dotnet-uwp-10.0) and [System.Collections.Specialized.INotifyCollectionChanged](https://docs.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged?view=dotnet-uwp-10.0) for C# apps. Instead, use the ```Microsoft.UI.Xaml.Interop``` versions of these interfaces
* [ThemeShadow](https://docs.microsoft.com/uwp/api/windows.ui.xaml.media.themeshadow)
* [WebView](https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.WebView)
* [Window.SetTitleBar](https://docs.microsoft.com/uwp/api/windows.ui.xaml.window.settitlebar) and custom window title bars
* [Xaml Islands](https://docs.microsoft.com/windows/apps/desktop/modernize/xaml-islands) functionality including [DesktopWindowXamlSource](https://docs.microsoft.com/uwp/api/windows.ui.xaml.hosting.desktopwindowxamlsource)
* [XamlLight](https://docs.microsoft.com/uwp/api/windows.ui.xaml.media.xamllight)

### Developer tools

* The Design view for Xaml files in Visual Studio is currently disabled for WinUI 3.0 apps.
* Live Visual Tree and other debugging tools may not function correctly for WinUI 3.0 apps.
* When Visual Studio automatically generates a code-behind event handler from Xaml markup (for example, events such as `Button.Click`), the namespace of the generated event args incorrectly start with `Windows.UI.Xaml` instead of `Microsoft.UI.Xaml`. You can fix this by manually changing the namespaces from `Windows.UI.Xaml` to  `Microsoft.UI.Xaml`.
* When editing XAML in Visual Studio, the g.cs and g.i.cs files are not generated on the fly. This means you have to build the project to get Intellisense for named elements in the codebehind file (see also [this issue](https://github.com/microsoft/microsoft-ui-xaml/issues/1534))

### Interactivity

* Multi-touch interactions on a touchscreen or precision touchpad can make scrolling and touch responsiveness unpredictable within the app and should be avoided at this time.

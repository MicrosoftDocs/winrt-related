---

description: Learn which features of the Windows API can be used in a Universal Windows Platform (UWP) app and which APIs to use as alternatives for those that cannot.
title: Alternatives to Windows APIs in Universal Windows Platform (UWP) apps

ms.topic: article


keywords: windows 10, uwp, win32, COM, alternatives
ms.date: 05/24/2017
ms.assetid: 5F130082-8F18-483A-8445-C829E9AFE26D
---

# Alternatives to Windows APIs in Universal Windows Platform (UWP) apps

Learn which features of the Windows API can be used in a Universal Windows Platform (UWP) app and which APIs to use as alternatives for those that cannot.

## App installation
None of the existing app installation APIs are supported in a UWP app. Here's some alternatives to the app installation APIs:

-   [Windows.ApplicationModel.Package](/uwp/api/Windows.ApplicationModel.Package) class
-   [Windows.Management.Deployment](/uwp/api/Windows.Management.Deployment) namespace

## Devices
A subset of the device APIs is supported in a UWP app.

For device APIs that cannot be used in a UWP app, here are some alternatives.

| Feature | Alternative |
|-----|--------------|
| Bluetooth | [Windows.Devices.Bluetooth](/uwp/api/windows.devices.bluetooth) |
| Device enumeration (Function Discovery, PnP-X, WSD) | [Windows.Devices.Enumeration](/uwp/api/Windows.Devices.Enumeration) |
| FAX | none |
| Location API | [Windows.Devices.Geolocation](/uwp/api/Windows.Devices.Geolocation) |
| Print | [Windows.Graphics.Printing](/uwp/api/Windows.Graphics.Printing) |
| 3D Printing | [Windows.Graphics.Printing3D](/uwp/api/Windows.Graphics.Printing3D) |
| Sensors | [Windows.Devices.Sensors](/uwp/api/Windows.Devices.Sensors) |
| Serial and parallel ports | [Windows.Devices.SerialCommunication](/uwp/api/Windows.Devices.SerialCommunication) |
| SMS | [Windows.Devices.Sms](/uwp/api/Windows.Devices.Sms) |
| UPnP | [Windows.Devices.Enumeration.Pnp](/uwp/api/Windows.Devices.Enumeration.Pnp) |
| Windows Portable Devices | [Windows.Devices.Portable](/uwp/api/Windows.Devices.Portable) |
| WSD | [Windows.Devices.Enumeration](/uwp/api/Windows.Devices.Enumeration) |
| Battery | [Windows.Devices.Power](/uwp/api/Windows.Devices.Power)<br />[Windows.System.Power](/uwp/api/Windows.System.Power) |

## Graphics
Subsets of these graphics APIs are at least partially supported in a UWP app:

-   Direct2D
-   Direct3D 11
-   DirectWrite
-   DirectXMath
-   DXGI
-   WIC

Here are some alternatives:
-   [Design](https://developer.microsoft.com/windows/apps/design)
-   [DirectX programming](/windows/uwp/gaming/directx-programming)
-   [Direct3D Graphics Learning Guide](/windows/uwp/graphics-concepts/)
-   [Graphics and animation](/windows/uwp/graphics/index)

## Multimedia
Subsets of these multimedia APIs are at least partially supported in a UWP app:

-   Core audio
-   Media Playback
-   Media Foundation
-   Windows Audio Session API (WASAPI)

For more information on API that are available for UWP apps, see [Audio, video, and camera](/windows/uwp/audio-video-camera/)

## Networking
Subsets of these networking APIs are at least partially supported in a UWP app:

-   DHCP
-   Mobile Broadband
-   RPC
-   Windows Sockets (Winsock)
-   Windows Web Services

Here's some alternatives to networking APIs that cannot be used in a UWP app.

| Feature     | Alternative                                                                                                                                                |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BITS        | [Windows.Networking.BackgroundTransfer](/uwp/api/Windows.Networking.BackgroundTransfer)                                                        |
| EAP | none |
| Firewall | none |
| HTTP Server | none |
| IP Helper   | [Windows.Networking.Connectivity](/uwp/api/Windows.Networking.Connectivity)                                                                          |
| NDF | none |
| NLM         | [Windows.Networking.Connectivity](/uwp/api/Windows.Networking.Connectivity)                                                                          |
| P2P | none |
| QOS         | [Windows.Networking.Sockets](/uwp/api/Windows.Networking.Sockets)                                                                                    |
| RAS | none |
| SNMP | none |
| TAPI | none |
| WinHTTP     | [Windows.Web.Http](/uwp/api/Windows.Web.Http)|
| WinINet     | [Windows.Web.Http](/uwp/api/Windows.Web.Http)  |
| Winsock     | [Windows.Networking.Sockets](/uwp/api/Windows.Networking.Sockets)                                                                                    |

## Printing and documents
A subset of the printing and documents APIs is supported in a UWP app.

When designing a UWP app, you'll want to provide the best printing experience:

-   [Printing](/windows/uwp/devices-sensors/printing-and-scanning)

## Security
None of the existing security APIs are supported in a UWP app. Here's some alternatives to the security APIs:

- [Windows.Security.Credentials](/uwp/api/Windows.Security.Credentials)
- [Windows.Security.Credentials.UI](/uwp/api/Windows.Security.Credentials.UI)
- [Windows.Security.Cryptography](/uwp/api/Windows.Security.Cryptography)
- [Windows.Security.Cryptography.Certificates](/uwp/api/Windows.Security.Cryptography.Certificates)
- [Windows.Security.Cryptography.Core](/uwp/api/Windows.Security.Cryptography.Core)
- [Windows.Security.Cryptography.DataProtection](/uwp/api/Windows.Security.Cryptography.DataProtection)

## Storage
Subsets of these storage APIs are at least partially supported in a UWP app:

-   Directory create, delete, and enumerate
-   File mapping

Here's some alternatives to Win32 storage APIs that cannot be used in a UWP app.

| Feature                                   | Alternative                                                           |
|-------------------------------------------|-----------------------------------------------------------------------|
| File copy, move, and replace              | [Windows.Storage.StorageFile](/uwp/api/Windows.Storage.StorageFile)              |
| Directory create, delete, and enumerate   | [Windows.Storage.StorageFolder](/uwp/api/Windows.Storage.StorageFolder)          |
| IMAPI                                     | none                                                                  |
| Management (mount points, format, quotas) | none                                                                  |
| Oplocks                                   | none                                                                  |
| Search                                    | [Windows.Storage.Search](/uwp/api/Windows.Storage.Search) |
| USN journal                               | none                                                                  |

 

## System
Subsets of these system APIs are at least partially supported in a UWP app:

-   Heap API, thread local storage (TLS)
-   Last error
-   Synchronization

Here's some alternatives to system APIs that cannot be used in a UWP app.

| Feature                                   | Alternative                                                           |
|-------------------------------------------|-----------------------------------------------------------------------|
| Console | [Create a UWP Console App](/windows/uwp/launch-resume/console-uwp) |
| Current directory | none |
| Fibers | none |
| Memory manager | Heap API | 
| Named pipes | [Interprocess Communications](/windows/win32/ipc/interprocess-communications) |
| Power | [Windows.Devices.Power](/uwp/api/Windows.Devices.Power)<br />[Windows.System.Power](/uwp/api/Windows.System.Power)<br />[Windows.System.Power.Diagnostics](/uwp/api/Windows.System.Power.Diagnostics) |
| Registry | [Windows.Storage.ApplicationDataContainer](/uwp/api/Windows.Storage.ApplicationDataContainer)<br />[Windows.Storage.ApplicationDataContainerSettings](/uwp/api/Windows.Storage.ApplicationDataContainerSettings)|
| Thread pool | [Windows.System.Threading](/uwp/api/Windows.System.Threading) |
| Threads | [Windows.System.Threading](/uwp/api/Windows.System.Threading) |


## User interface
Subsets of these user interface APIs are at least partially supported in a UWP app:

-   National Language Support (NLS)
-   Strsafe functions
-   Text Services Framework (TSF)
-   UI automation
-   Windows Animation Manager

Here's some alternatives to user interface APIs that cannot be used in a UWP app.

| Feature                                   | Alternative                                                           |
|-------------------------------------------|-----------------------------------------------------------------------|
Common controls | HTML, XAML |
DDE/NetDDE | none |
DWM | [Windows.UI.Composition](/uwp/api/windows.ui.composition) |
File Open, File Save | [Windows.Storage.Pickers.FileOpenPicker](/uwp/api/Windows.Storage.Pickers.FileOpenPicker)<br />[Windows.Storage.Pickers.FileSavePicker](/uwp/api/Windows.Storage.Pickers.FileSavePicker) |
IMM | TSF |
Magnifier | none |
MSAA | UI automation |
NLS | [Windows.Globalization](/uwp/api/Windows.Globalization)<br />[Windows.Globalization.DateTimeFormatting](/uwp/api/Windows.Globalization.DateTimeFormatting)<br />[Windows.Globalization.NumberFormatting](/uwp/api/Windows.Globalization.NumberFormatting) |
RichEdit | HTML, XAML |
Theming | HTML, CSS, XAML |
Touch | [Windows.UI.Input](/uwp/api/Windows.UI.Input) |
User: carets | framework or app to draw |
User: cursors | [Windows.UI.Core.CoreCursor](/uwp/api/Windows.UI.Core.CoreCursor) |
User: clipboard | [Windows.ApplicationModel.DataTransfer.Clipboard](/uwp/api/Windows.ApplicationModel.DataTransfer.Clipboard) |
User: controls | HTML, XAML |
User: display | [Windows.Graphics.Display](/uwp/api/Windows.Graphics.Display) |
User: high DPI | apps are DPI aware |
User: hooks | none |
User: icons | apps represented by tiles |
User: keyboard accel | [Windows.UI.Core.CoreAcceleratorKeys](/uwp/api/Windows.UI.Core.CoreAcceleratorKeys) |
User: keyboard input | [Windows.Devices.Input](/uwp/api/Windows.Devices.Input) |
User: MDI | [TabView XAML Control](/windows/communitytoolkit/controls/tabview), [AppWindow](/uwp/api/windows.ui.windowmanagement.appwindow) |
User: messages | events and notifications |
User: mouse input | [Windows.Devices.Input](/uwp/api/Windows.Devices.Input) |
User: multimon | single monitor |
User: SystemParametersInfo | [Windows.Devices.Input](/uwp/api/Windows.Devices.Input) |
User: strings | strsafe functions |
User: timers | none |
User: shutdown | none |
User: windowing | [Windows.UI.Core.CoreWindow](/uwp/api/Windows.UI.Core.CoreWindow)<br />[Windows.UI.Core.CoreWindowDialog](/uwp/api/Windows.UI.Core.CoreWindowDialog)<br />[Windows.UI.Core.CoreWindowFlyout](/uwp/api/Windows.UI.Core.CoreWindowFlyout) |
Windows Animation Manager | [Windows.UI.Core.AnimationMetrics](/uwp/api/Windows.UI.Core.AnimationMetrics) |
Windows Ribbon | HTML, XAML |

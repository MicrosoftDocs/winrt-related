---
title: What's different in Windows 10
description: This topic lists changes to the package manifest schema reference for Windows 10, including elements that have been added, removed, and changed.
ms.assetid: 2afadf58-6dcc-4959-b97b-47d2075af692
author: laurenhughes
ms.author: lahugh
ms.topic: article
ms.prod: windows
ms.technology: uwp

keywords: windows 10, uwp, schema, package manifest
---

# What's different in Windows 10


This topic lists changes to the package manifest schema reference for Windows 10, including elements that have been added, removed, and changed. See [Element Hierarchy](root-elements.md) for reference info on all elements, attributes, and types in the schema.

## Elements and attributes that have been added


-   [**uap:Capability**](element-uap-capability.md) element (and its child elements). Valid values for the uap:Capability@Name attribute are "documentsLibrary", "picturesLibrary", "videosLibrary", "musicLibrary", "enterpriseAuthentication", "sharedUserCertificates", "userAccountInformation", "removableStorage", "appointments", "contacts", "phoneCall", and "blockedChatMessages". See [App capability declarations](https://msdn.microsoft.com/library/windows/apps/hh464936).
-   [**uap:Extension**](element-uap-extension.md) element. Valid values for the uap:Extension@Category attribute are "windows.webAccountProvider", "windows.dialProtocol", "windows.appService", "windows.mediaPlayback", and "windows.print3DWorkflow".
-   [**PublisherCacheFolders**](element-publishercachefolders.md) element.
-   [**uap:SupportedUsers**](element-uap-supportedusers.md) element.
-   [**uap:Task**](element-uap-task.md) element. Valid values for the @Type attribute are "chatMessageNotification", "vpnClient", "phoneCall", and "mediaProcessing".
-   [**Application@ResourceGroup**](element-application.md) attribute.
-   [**uap:FileTypeAssociation@DesiredView**](element-uap-filetypeassociation.md) attribute.
-   [**uap:Protocol@DesiredView**](element-uap-protocol.md) attribute.
-   [**uap:Protocol@ReturnResults**](element-uap-protocol.md) attribute.
-   [**uap:Rule@WindowsRuntimeAccess**](element-uap-rule.md) attribute.
-   [**uap:VisualElements@AppListEntry**](element-uap-visualelements.md) attribute.

## Elements and attributes that have changed


-   The [**uap:ApplicationContentUriRules**](element-uap-applicationcontenturirules.md) element (and its child elements) is now in an xml namespace that uses the "uap:" xml namespace prefix.
-   For the [**Capability**](element-capability.md) element, some values for the @Name attribute have moved to the new [**uap:Capability**](element-uap-capability.md) element. Valid values for **Capability@Name** are now "internetClient", "internetClientServer", "privateNetworkClientServer", and "allJoyn". See [App capability declarations](https://msdn.microsoft.com/library/windows/apps/hh464936).
-   For the [**Extension**](element-1-extension.md) element, some values for the @Category attribute have moved to the new [**uap:Extension**](element-uap-extension.md) element. For **Extension@Category**, new valid values are "windows.preInstalledConfigTask", "windows.updateTask", and "windows.restrictedLaunch". The values "windows.contactPicker" and "windows.contact" have been removed.
-   The Application/Extensions/Extension/[**uap:FileTypeAssociation**](element-uap-filetypeassociation.md) element is now in an xml namespace that uses the "uap:" xml namespace prefix.
-   The Application/Extensions/Extension/[**uap:Protocol**](element-uap-protocol.md) element is now in an xml namespace that uses the "uap:" xml namespace prefix.
-   The Application/Extensions/Extension/[**uap:AutoPlayContent**](element-uap-autoplaycontent.md) element is now in an xml namespace that uses the "uap:" xml namespace prefix.
-   The Application/Extensions/Extension/[**uap:AutoPlayDevice**](element-uap-autoplaydevice.md) element is now in an xml namespace that uses the "uap:" xml namespace prefix.
-   The Application/Extensions/Extension/[**uap:ShareTarget**](element-uap-sharetarget.md) element is now in an xml namespace that uses the "uap:" xml namespace prefix.
-   The Application/Extensions/Extension/[**uap:FileOpenPicker**](element-uap-fileopenpicker.md) element is now in an xml namespace that uses the "uap:" xml namespace prefix.
-   The Application/Extensions/Extension/[**uap:FileSavePicker**](element-uap-filesavepicker.md) element is now in an xml namespace that uses the "uap:" xml namespace prefix.
-   The Application/Extensions/Extension/[**uap:AppointmentsProvider**](element-uap-appointmentsprovider.md) element is now in an xml namespace that uses the "uap:" xml namespace prefix.
-   The [**Application@StartPage**](element-application.md) attribute was previously required to be a relative Windows file path referencing a document in the app's package. Now it additionally may be an absolute URL (so that a web site can publish as an app in the Store).
-   For the [**DeviceCapability@Name**](element-devicecapability.md) attribute, new valid values are "bluetooth", "wiFiControl", "radios", and "optical". See [App capability declarations](https://msdn.microsoft.com/library/windows/apps/hh464936).
-   The [**PackageDependency@Publisher**](element-packagedependency.md) attribute is now required.
-   For the [**Task@Type**](element-task.md) attribute, new valid values are "general", "deviceConnectionChange", and "bluetooth".
-   The [**uap:VisualElements**](element-uap-visualelements.md) element (and its child elements) is now in an xml namespace that uses the "uap:" xml namespace prefix.
-   The [**VisualElements@Logo**](https://msdn.microsoft.com/library/windows/apps/dn423310) attribute has been renamed [**uap:VisualElements@Square150x150Logo**](element-uap-visualelements.md).
-   The [**VisualElements@Square30x30Logo**](https://msdn.microsoft.com/library/windows/apps/dn423310) attribute has been renamed [**uap:VisualElements@Square44x44Logo**](element-uap-visualelements.md).
-   The [**VisualElements@Square70x70Logo**](https://msdn.microsoft.com/library/windows/apps/dn423310) attribute has been renamed [**uap:VisualElements@Square71x71Logo**](element-uap-visualelements.md).

## Elements and attributes that have been removed


-   [**ApplicationView**](https://msdn.microsoft.com/library/windows/apps/dn391667) element.
-   [**Prerequisites**](https://msdn.microsoft.com/library/windows/apps/dn423292) element.
-   [**VisualElements@DefaultSize**](https://msdn.microsoft.com/library/windows/apps/dn423310) attribute.
-   [**VisualElements@ForegroundText**](https://msdn.microsoft.com/library/windows/apps/dn423310) attribute.
-   [**VisualElements@SmallLogo**](https://msdn.microsoft.com/library/windows/apps/dn423310) attribute.
-   [**VisualElements@ToastCapable**](https://msdn.microsoft.com/library/windows/apps/dn423310) attribute.

 

 




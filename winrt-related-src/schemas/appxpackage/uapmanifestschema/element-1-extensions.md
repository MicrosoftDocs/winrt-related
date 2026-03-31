---
description: Defines one or more extensibility points for the app (Windows 10) by detailing the element hierarchy and syntax.
Search.Product: eADQiWindows 10XVcnh
title: Extensions (in Application)
ms.assetid: 267051e3-b09c-467c-b5bd-4575cc31cb36
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
no-loc: [Package, Applications, Application, Extensions]
---

# Extensions (in Application)

Defines one or more extensibility points for the app.

## Element hierarchy

**[`<Package>`](element-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Extensions>`**  

## Syntax

```xml
<Extensions>

  <!-- Child elements -->
  Extension{1,10000}

</Extensions>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| Extension | Declares an extensibility point for the app. The type of extension is defined by the **Category** attribute. See the extension category table in the [Remarks](#remarks) section below for the list of allowed categories and the Extension element that defines each one. |

### Parent elements

| Parent element | Description |
|---------------|-------------|
| [Application](element-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

## See also
The following elements have the same name as this one, but different content or attributes:

- **[Extensions (type: CT_PackageExtensions)](element-extensions.md)**

## Remarks

Extensibility points are a mechanism by which an app can add functionality in a manner defined by the operating system. An example of an app extensibility point is the ability to create a file type association and enable your app to be the default handler for files with a specific file name extension.

The **Extension** elements that can be included under the **Application/Extensions** element are enforced by the XML schema. Each of these **Extension** elements have a required **Category** attribute that specifies one or more extension points that the extension supports. Some extensions support both application and package extension categories. The following table lists the extension categories supported for application extensions and the associated **Extension** element that supports each category. A category can be supported for multiple extensions as a versioning mechanism.

| Extension category | Extension |
|--------------------|-----------|
| windows.aboveLockScreen | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.accountPictureProvider | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.activatableClass.outOfProcessServer | [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.alarm | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.appExecutionAlias | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual), [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.appExtension | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.appExtensionHost | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.applicationRegistration | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.appointmentDataProvider | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.appointmentsProvider | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.appPrinter | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-extension) |
| windows.approvedShellExtension | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.appService | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension), [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.appUriHandler | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.autoPlayContent | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.autoPlayDevice | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.autoPlayHandler | [desktop3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop3-extension) |
| windows.backgroundTasks | [f:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-1-extension) |
| windows.barcodeScannerPreviewProvider | [uap6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap6-extension) |
| windows.barcodeScannerProvider | [uap6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap6-extension) |
| windows.cachedFileUpdater | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.cameraSettings | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.cloudFiles | [cloudFiles:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-cloudfiles-extension), [desktop3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop3-extension) |
| windows.comInterface | [com:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com-extension), [com2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com2-extension), [com4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com4-extension) |
| windows.comServer | [com:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com-extension), [com2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com2-extension), [com4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com4-extension) |
| windows.contactDataProvider | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.contactPanel | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.controlPanelItem | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.desktopAppMigration | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension), [rescap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap3-extension) |
| windows.devicePortalProvider | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.dialProtocol | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.emailDataProvider | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.errorReporting | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.fileExplorerContextMenus | [desktop4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop4-extension) |
| windows.fileOpenPicker | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.fileSavePicker | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.fileTypeAssociation | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension), [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.fullTrustProcess | [desktop:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop-extension) |
| windows.localExperiencePack | [uap6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap6-extension) |
| windows.lockScreen | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.lockScreenCall | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.lockScreenComponent | [rescap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap3-extension) |
| windows.loopbackAccessRules | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.mailProvider | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-extension), [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.mediaCodec | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.mediaPlayback | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.mediaSource | [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.personalAssistantLaunch | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.phoneCallActivation | [uap13:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap13-extension) |
| windows.posPaymentConnector | [uap8:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap8-extension) |
| windows.preInstalledConfigTask | [f:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-1-extension) |
| windows.print3DWorkflow | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.printSupportEnterpriseManagementUI | printSupport3:Extension |
| windows.printSupportExtension | [printSupport:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-printsupport-extension), [uap12:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap12-extension) |
| windows.printSupportJobUI | [printSupport:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-printsupport-extension), [uap12:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap12-extension) |
| windows.printSupportSettingsUI | [printSupport:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-printsupport-extension), [uap12:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap12-extension) |
| windows.printSupportVirtualPrinterWorkflow | [printSupport2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-printsupport2-extension) |
| windows.printSupportWorkflow | [printSupport:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-printsupport-extension), [uap12:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap12-extension) |
| windows.printTaskSettings | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.printWorkflowBackgroundTask | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.printWorkflowForegroundTask | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.protocol | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension), [uap10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap10-extension), [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.restrictedLaunch | [f:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-1-extension) |
| windows.search | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.searchFilterHandler | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-extension) |
| windows.searchPropertyHandler | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-extension) |
| windows.searchProtocolHandler | [desktop:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop-extension) |
| windows.service | [desktop6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop6-extension), [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.settingsApp | [rescap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap-extension) |
| windows.shadowCopyExcludeFiles | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.sharedFonts | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.shareTarget | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.shortcut | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.startupTask | [desktop:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop-extension), [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.systemFileAssociation | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.toastNotificationActivation | [desktop:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop-extension) |
| windows.updateTask | [f:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-1-extension) |
| windows.userActivity | [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.userDataTaskDataProvider | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.videoRendererEffect | [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.voipCall | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.webAccountProvider | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension), [uap2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap2-extension) |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |

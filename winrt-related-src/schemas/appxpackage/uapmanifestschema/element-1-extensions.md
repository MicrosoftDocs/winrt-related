---
description: Defines one or more extensibility points for the app (Windows 10) by detailing the element hierarchy and syntax.
Search.Product: eADQiWindows 10XVcnh
title: Extensions (in Application) (Windows 10)
ms.assetid: 267051e3-b09c-467c-b5bd-4575cc31cb36
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Extensions (in Application) (Windows 10)

Defines one or more extensibility points for the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Extensions\>**

## Syntax

```xml
<Extensions>

  <!-- Child elements -->
  Extension{1,10000},
  cloudFiles:Extension{1,10000},
  com2:Extension{1,10000},
  com4:Extension{1,10000},
  com:Extension{1,10000},
  desktop2:Extension{1,10000},
  desktop3:Extension{1,10000},
  desktop4:Extension{1,10000},
  desktop6:Extension{1,10000},
  desktop7:Extension{1,10000},
  desktop9:Extension{1,10000},
  desktop:Extension{1,10000},
  mobile:Extension{1,10000},
  printSupport:Extension{1,10000},
  rescap3:Extension{1,10000},
  rescap:Extension{1,10000},
  uap10:Extension{1,10000},
  uap12:Extension{1,10000},
  uap13:Extension{1,10000},
  uap2:Extension{1,10000},
  uap3:Extension{1,10000},
  uap4:Extension{1,10000},
  uap5:Extension{1,10000},
  uap6:Extension{1,10000},
  uap7:Extension{1,10000},
  uap:Extension{1,10000}

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
| [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-1-extension) | Declares an extensibility point for the app. |
| [cloudFiles:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-cloudfiles-extension) | Declares an extensibility point for the app. |
| [com2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com2-extension) | Declares an extensibility point for the app. |
| [com4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com4-extension) | Declares an extensibility point for the app. |
| [com:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com-extension) | Declares an extensibility point for the app. |
| [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-extension) | Declares an extensibility point for the app. |
| [desktop3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop3-extension) | Declares an extensibility point for the app. |
| [desktop4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop4-extension) | Declares an extensibility point for the app. |
| [desktop6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop6-extension) | Declares an extensibility point for the app. |
| [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) | Declares an extensibility point for the app. |
| [desktop9:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop9-extension) | Declares an extensibility point for the app. |
| [desktop:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop-extension) | Declares an extensibility point for the app. |
| [mobile:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-mobile-extension-manual) | Declares an extensibility point for the app. |
| [printSupport:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-printsupport-extension) | Declares an extensibility point for the app. |
| [rescap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap3-extension) | Declares an extensibility point for the app. |
| [rescap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap-extension) | Declares an extensibility point for the app. |
| [uap10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap10-extension) | Declares an extensibility point for the app. |
| [uap12:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap12-extension) | Declares an extensibility point for the app. |
| [uap13:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap13-extension) | Declares an extensibility point for the app. |
| [uap2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap2-extension) | Declares an extensibility point for the app. |
| [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) | Declares an extensibility point for the app. |
| [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) | Declares an extensibility point for the app. |
| [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) | Declares an extensibility point for the app. |
| [uap6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap6-extension) | Declares an extensibility point for the app. |
| [uap7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap7-extension) | Declares an extensibility point for the app. |
| [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) | Declares an extensibility point for the app. |

### Parent elements

| Parent element | Description |
|---------------|-------------|
| [Application](element-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- **[Extensions (type: CT_PackageExtensions)](element-extensions.md)**

## Remarks

Extensibility points are a mechanism by which an app can add functionality in a manner defined by the operating system. An example of an app extensibility point is the ability to create a file type association and enable your app to be the default handler for files with a specific file name extension.

The **Extension** elements that can be included under the **Application/Extensions** element are enforced by the XML schema. Each of these **Extension** elements have a required **category** attribute that specifies one or more extension points that the extension supports. Some extensions support both application and package extension categories. The following table lists the extension categories supported for application extensions and the associated **Extension** element that supports each category. A category can be supported for multiple extensions as a versioning mechanism.

| Extension category | Extension |
|--------------------|-----------|
| windows.backgroundTasks | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-1-extension) |
| windows.preInstalledConfigTask | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-1-extension) |
| windows.updateTask | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-1-extension) |
| windows.restrictedLaunch | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-1-extension) |
| windows.cloudFiles | [cloudFiles:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-cloudfiles-extension) |
| windows.comServer | [com:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com-extension) |
| windows.comInterface | [com:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com-extension) |
| windows.comServer | [com2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com2-extension) |
| windows.comInterface | [com2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com2-extension) |
| windows.comServer | [com4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com4-extension) |
| windows.comInterface | [com4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com4-extension) |
| windows.fullTrustProcess | [desktop:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop-extension) |
| windows.startupTask | [desktop:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop-extension) |
| windows.toastNotificationActivation | [desktop:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop-extension) |
| windows.searchProtocolHandler | [desktop:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop-extension) |
| windows.appPrinter | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-extension) |
| windows.searchFilterHandler | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-extension) |
| windows.searchPropertyHandler | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-extension) |
| windows.mailProvider | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-extension) |
| windows.autoPlayHandler | [desktop3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop3-extension) |
| windows.cloudFiles | [desktop3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop3-extension) |
| windows.fileExplorerContextMenus | [desktop4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop4-extension) |
| windows.service | [desktop6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop6-extension) |
| windows.approvedShellExtension | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.controlPanelItem | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.service | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.mailProvider | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.shortcut | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.applicationRegistration | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.desktopAppMigration | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.systemFileAssociation | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.shadowCopyExcludeFiles | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.shadowCopyExcludeFiles | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-package-extension) |
| windows.fileExplorerClassicContextMenuHandler | [desktop9:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop9-extension) |
| windows.fileExplorerClassicDragDropContextMenuHandler | [desktop9:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop9-extension) |
| windows.activatableClass.outOfProcessServer | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-extension) |
| windows.comInterface | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-extension) |
| windows.aowApp | [mobile:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-mobile-extension-manual) |
| windows.mobileMultiScreenProperties | [mobile:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-mobile-extension-manual) |
| windows.communicationBlockingProvider | [mobile:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-mobile-extension-manual) |
| windows.phoneCallOriginProvider | [mobile:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-mobile-extension-manual) |
| windows.printSupportSettingsUI | [ printSupport:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-printsupport-extension) |
| windows.printSupportExtension | [ printSupport:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-printsupport-extension) |
| windows.printSupportJobUI | [ printSupport:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-printsupport-extension) |
| windows.settingsApp | [rescap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap-extension) |
| windows.desktopAppMigration | [rescap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap3-extension) |
| windows.lockScreenComponent | [rescap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap3-extension) |
| windows.fileTypeAssociation | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.protocol | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.autoPlayContent | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.autoPlayDevice | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.shareTarget | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.search | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.fileOpenPicker | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.fileSavePicker | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.cachedFileUpdater | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.cameraSettings | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.accountPictureProvider | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.printTaskSettings | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.lockScreenCall | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.appointmentsProvider | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.alarm | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.webAccountProvider | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.dialProtocol | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.appService | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.mediaPlayback | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.print3DWorkflow | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.lockScreen | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.aboveLockScreen | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.personalAssistantLaunch | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.voipCall | [uap:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap-extension) |
| windows.protocol | [uap10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap10-extension) |
| windows.printSupportSettingsUI | [uap12:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap12-extension) |
| windows.printSupportExtension | [uap12:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap12-extension) |
| windows.printSupportJobUI | [uap12:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap12-extension) |
| windows.phoneCallActivation | [uap13:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap13-extension) |
| windows.webAccountProvider | [uap2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap2-extension) |
| windows.appointmentDataProvider | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.emailDataProvider | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.contactDataProvider | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.appUriHandler | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.appExtensionHost | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.appExtension | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.protocol | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.fileTypeAssociation | [uap3:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap3-extension-manual) |
| windows.sharedFonts | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.userDataTaskDataProvider | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.mediaCodec | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.contactPanel | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.loopbackAccessRules | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.devicePortalProvider | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.printWorkflowBackgroundTask | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.printWorkflowForegroundTask | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.userActivity | [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.mediaSource | [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.videoRendererEffect | [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.activatableClass.outOfProcessServer | [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.startupTask | [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.appExecutionAlias | [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.barcodeScannerProvider | [uap6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap6-extension) |
| windows.barcodeScannerPreviewProvider | [uap6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap6-extension) |
| windows.localExperiencePack | [uap6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap6-extension) |
| windows.sharedFonts | [uap7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap7-extension) |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |

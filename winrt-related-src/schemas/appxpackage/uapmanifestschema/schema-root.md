---
Description: Provides details for each element, attribute, and data type that defines the schema for the app package manifest for Windows 10 apps. 
Search.Product: eADQiWindows 10XVcnh
title: Package manifest schema reference for Windows 10
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 05/17/2017
---

# Package manifest schema reference for Windows 10


This reference provides details for each element, attribute, and data type that defines the schema for the app package manifest for Windows 10 apps. The schema definition files are UapManifestSchema.xsd, FoundationManifestSchema.xsd, AppxManifestTypes.xsd, and others.

UapManifestSchema.xsd and FoundationManifestSchema.xsd import one another's namespaces, and they both import the namespace of AppxManifestTypes.xsd.

The following table lists all of the elements in this schema, sorted alphabetically by name.

| Element | Description |
|---------|-------------|
| [ActivatableClass (type: CT_InProcessActivatableClass)](element-activatableclass.md) | Declares a runtime class associated with the extensibility point. |
| [ActivatableClass (type: CT_OutOfProcessActivatableClass)](element-1-activatableclass.md) | Declares a runtime class associated with the extensibility point. |
| [ActivatableClassAttribute](element-activatableclassattribute.md) | Defines an attribute of the class that is stored in the Windows Runtime property store. |
| [Application](element-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |
| [Applications](element-applications.md) | Represents one or more apps that comprise the package. |
| [Arguments](element-arguments.md) | Specifies the list of comma-separated arguments to pass to the executable. |
| [BackgroundTasks](element-backgroundtasks.md) | Defines an app extensibility point of type **windows.backgroundTasks**. Background tasks run in a dedicated background host; that is, without a UI. |
| [Capabilities](element-capabilities.md) | Declares the access to protected user resources that the package requires. |
| [Capability](element-capability.md) | Declares a capability required by a package. |
| [Certificate](element-certificate.md) | A certificate for use with the package and placed in the system certificate stores. |
| [Certificates](element-certificates.md) | Declares a package extensibility point of type **windows.certificates**. The app requires one or more certificates from the specified certificate stores. |
| [Dependencies](element-dependencies.md) | Declares other packages that a package depends on to complete its software. |
| [Description](element-description.md) | A friendly description that can be displayed to users. |
| [Device](element-device.md) | Declares a function for a device that is associated with the [**DeviceCapability**](element-devicecapability.md). On Windows 10.0.10240.0, a **DeviceCapability** can contain up to 100 **Device** elements. On Windows 10.0.10586.0, it can contain up to 1000 (for more details, see **DeviceCapability**). |
| [DeviceCapability](element-devicecapability.md) | Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 [**Device**](element-device.md) elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples). |
| [DisplayName](element-displayname.md) | A friendly name that can be displayed to users. |
| [Extension (global)](element-1-extension.md) | Declares an extensibility point for the package. |
| [Extension (in type: CT_PackageExtensions)](element-extension.md) | Declares an extensibility point for the package. |
| [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the app. |
| [Extensions (type: CT_PackageExtensions)](element-extensions.md) | Defines one or more extensibility points for the package. |
| [Folder](element-folder.md) | Specifies a folder that the package shares with other packages from the same publisher. |
| [Framework](element-framework.md) | Indicates whether the package is a framework package; that is, a package that can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a framework. |
| [Function](element-function.md) | Declares the function for the device. |
| [Identity](element-identity.md) | Defines a globally unique identifier for a package. A package identity is represented as a tuple of attributes of the package. |
| [InProcessServer](element-inprocessserver.md) | Declares a package extensibility point of type **windows.activatableClass.inProcessServer**. The app uses a dynamic link library (DLL) that exposes one or more activatable classes. |
| [Instancing](element-instancing.md) | Specifies whether the executable runs as a single instance or can run as multiple instances. |
| [Interface](element-interface.md) | Declares an interface associated with the proxy. |
| [Logo](element-logo.md) | A path to a file that contains an image. |
| [OutOfProcessServer](element-outofprocessserver.md) | Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. The app uses an executable (EXE) that exposes one or more activatable classes. |
| [Package](element-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |
| [PackageDependency](element-packagedependency.md) | Declares a dependency on another package that is marked as a framework package. |
| [Path (type: ST_Executable)](element-1-path.md) | The path to the executable. |
| [Path (type: ST_FileName)](element-path.md) | The path to the DLL. |
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. **Note:**  You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely “&#124;” and “all”, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](https://msdn.microsoft.com/library/windows/desktop/hh973484) if you get an error. |
| [ProxyStub](element-proxystub.md) | Declares a package extensibility point of type **windows.activatableClass.proxyStub**. A proxy can be composed of one or more interfaces. |
| [PublisherCacheFolders](element-publishercachefolders.md) | Declares a package extensibility point of type **windows.publisherCacheFolders**. This specifies one or more folders that the package shares with other packages from the same publisher. |
| [PublisherDisplayName](element-publisherdisplayname.md) | A friendly name for the publisher that can be displayed to users. |
| [Resource](element-resource.md) | Declares a language for the resource contained in the package. The scale and DirectX feature level attributes are common for all resources in the package. |
| [ResourcePackage](element-resourcepackage.md) | Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a resource. |
| [Resources](element-resources.md) | Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package. |
| [SelectionCriteria](element-selectioncriteria.md) | Defines selection criteria for the certificates defined for the package. |
| [TargetDeviceFamily](element-targetdevicefamily.md) | Identifies the device family that your package targets. For more info about device families, see [Guide to UWP apps](https://msdn.microsoft.com/library/windows/apps/dn894631). |
| [Task](element-task.md) | The background task associated with the app extensibility point. |
| [TrustFlags](element-trustflags.md) | Indicates whether the certificates for the package are exclusive to the package. |
| [pm:PhoneIdentity](element-pm-phoneidentity.md) | If your app is an update to an app previously made available on Windows Phone, ensure that this element matches what is in the app manifest of your previous app. Use the same GUIDs that were assigned to the app by the Store. This ensures that users of your app who are upgrading to Windows 10 will receive your new app as an update, and not as a duplicate. |
| [uap:AppService](element-uap-appservice.md) | Declares an app extensibility point of type **windows.appService**. Application Contracts are a way for an app to invoke a background task belonging to another app; or for a background task invoked to service an app contract a way to communicate with its caller. |
| [uap:ApplicationContentUriRules](element-uap-applicationcontenturirules.md) | Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard. |
| [uap:AppointmentsProvider](element-uap-appointmentsprovider.md) | Declares an app extensibility point of type **windows.appointmentsProvider**. |
| [uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md) | Declares actions to take when a appointment is launched. |
| [uap:AutoPlayContent](element-uap-autoplaycontent.md) | Declares an app extensibility point of type **windows.autoPlayContent**. The app provides the specified AutoPlay content actions. |
| [uap:AutoPlayDevice](element-uap-autoplaydevice.md) | Declares an app extensibility point of type **windows.autoPlayDevice**. The app provides the specified AutoPlay device actions. |
| [uap:Capability](element-uap-capability.md) | Declares a capability required by a package. |
| [uap:Codec](element-uap-codec.md) | Specifies the codec to use for transcoding. |
| [uap:DataFormat](element-uap-dataformat.md) | Specifies a data package format such as text or HTML format that the app can share. It is unique per application in the package and is case sensitive. |
| [uap:DefaultTile](element-uap-defaulttile.md) | The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default. |
| [uap:DialProtocol](element-uap-dialprotocol.md) | Declares an app extensibility point of type **windows.dialProtocol**. |
| [uap:DisplayName](element-uap-displayname.md) | A friendly name that can be displayed to users. |
| [uap:EditFlags](element-uap-editflags.md) | Specifies the type of info the user sees when opening a file associated to the extensibility point. |
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |
| [uap:FileOpenPicker](element-uap-fileopenpicker.md) | Declares an app extensibility point of type **windows.fileOpenPicker**. The app lets the user choose and open the specified types of files. |
| [uap:FileSavePicker](element-uap-filesavepicker.md) | Declares an app extensibility point of type **windows.fileSavePicker**. The app lets the user choose the file name, extension, and storage location for the specified types of files. |
| [uap:FileType (in type: CT_FTASupportedFileTypes)](element-uap-filetype.md) | A supported file type specified as its file type extension. |
| [uap:FileType (type: ST_FileType)](element-1-uap-filetype.md) | A file type specified as its file type extension. It is unique per application in the package and is case sensitive. |
| [uap:FileTypeAssociation](element-uap-filetypeassociation.md) | Declares an app extensibility point of type **windows.fileTypeAssociation**. A file type association indicates that the app is registered to handle files of the specified types. |
| [uap:InfoTip](element-uap-infotip.md) | Defines a string that provides additional info to the user about the file type. |
| [uap:InitialRotationPreference](element-uap-initialrotationpreference.md) | Describes the orientations in which the app would prefer to be shown for the best user experience. |
| [uap:LaunchAction (global)](element-2-uap-launchaction.md) | Describes an [**uap:AppointmentsProviderLaunchActions**](element-uap-appointmentsproviderlaunchactions.md) content action. |
| [uap:LaunchAction (in type: CT_AutoPlayContent)](element-uap-launchaction.md) | Describes an AutoPlay content action. |
| [uap:LaunchAction (in type: CT_AutoPlayDevice)](element-1-uap-launchaction.md) | Describes an AutoPlay device action. |
| [uap:LockScreen](element-uap-lockscreen.md) | Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked. |
| [uap:Logo](element-uap-logo.md) | A path to a file that contains an image. |
| [uap:ManagedUrls](element-uap-managedurls.md) | Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies. |
| [uap:MediaPlayback](element-uap-mediaplayback.md) | Declares an app extensibility point of type **mediaPlayback** so that your app can declare that it performs video transcoding. |
| [uap:Protocol](element-uap-protocol.md) | Declares an app extensibility point of type **windows.protocol**. A URI association indicates that the app is registered to handle URIs with the specified scheme. |
| [uap:Rotation](element-uap-rotation.md) | Specifies a single rotational orientation in which an app will display. |
| [uap:Rule](element-uap-rule.md) | Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard. |
| [uap:ShareTarget](element-uap-sharetarget.md) | Declares an app extension point of type **windows.shareTarget**. The app can share the specified types of files. |
| [uap:ShowNameOnTiles](element-uap-shownameontiles.md) | Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen. |
| [uap:ShowOn](element-uap-showon.md) | Describes whether Windows overlays the app’s name on top of the tile image that is shown on the Start screen. |
| [uap:SplashScreen](element-uap-splashscreen.md) |  |
| [uap:SupportedFileTypes (type: CT_CharmsSupportedFileTypes)](element-1-uap-supportedfiletypes.md) | Defines the file types that the app can share. |
| [uap:SupportedFileTypes (type: CT_FTASupportedFileTypes)](element-uap-supportedfiletypes.md) | Defines the file types associated with the app. They are unique per package and are case sensitive. |
| [uap:SupportedUsers](element-uap-supportedusers.md) | Indicates whether or not the package is multi-user aware. This setting is used at install time to determine whether the package can be installed on the system. |
| [uap:SupportsAnyFileType](element-uap-supportsanyfiletype.md) | Indicates whether all file types are supported for sharing. |
| [uap:Task](element-uap-task.md) | The background task associated with the app extensibility point. |
| [uap:TileUpdate](element-uap-tileupdate.md) | Describes how the app tile receives update notifications. |
| [uap:Url](element-uap-url.md) | Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL. |
| [uap:VisualElements](element-uap-visualelements.md) | Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance. |
| [uap:VoipCall](element-uap-voipcall.md) | Declares an app extensibility point of type **voipCall** so that your app can declare that it can perform an upgrade from a cellular call to a VoIP video call, and/or whether it is a VoIP app that supports dialing phone numbers directly. |
| [uap:VoipCallUpgrade](element-uap-voipcallupgrade.md) | Indicates that the app supports video upgrade. Video upgrade is a feature on some mobile devices such that, when a user is on a cellular call, the user can upgrade that call to a VoIP video call if there is an app installed that can service such a request. These upgrades can be non-seamless (we must drop the cellular call before starting the video call through the app) or seamless (the cellular call remains connected until the app tells us the video call is established). |
| [uap:VoipDialPhoneNumber](element-uap-voipdialphonenumber.md) | Indicates that the app supports dialing phone numbers. |
| [uap:WebAccountProvider](element-uap-webaccountprovider.md) | Declares an app extensibility point of type **windows.webAccountProvider**. |

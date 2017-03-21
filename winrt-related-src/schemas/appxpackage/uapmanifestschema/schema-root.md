---
Description: Package manifest schema reference for Windows 10
Search.Product: eADQiWindows 10XVcnh
title: Package manifest schema reference for Windows 10
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, package manifest
---

# Package manifest schema reference for Windows 10


This reference provides details for each element, attribute, and data type that defines the schema for the app package manifest for Windows 10 apps. The schema definition files are UapManifestSchema.xsd, FoundationManifestSchema.xsd, AppxManifestTypes.xsd, and others.

UapManifestSchema.xsd and FoundationManifestSchema.xsd import one another's namespaces, and they both import the namespace of AppxManifestTypes.xsd.

The following table lists all of the elements in this schema, sorted alphabetically by name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[ActivatableClass (type: CT_InProcessActivatableClass)](element-activatableclass.md)</td>
<td><p>Declares a runtime class associated with the extensibility point.</p></td>
</tr>
<tr class="even">
<td>[ActivatableClass (type: CT_OutOfProcessActivatableClass)](element-1-activatableclass.md)</td>
<td><p>Declares a runtime class associated with the extensibility point.</p></td>
</tr>
<tr class="odd">
<td>[ActivatableClassAttribute](element-activatableclassattribute.md)</td>
<td><p>Defines an attribute of the class that is stored in the Windows Runtime property store.</p></td>
</tr>
<tr class="even">
<td>[Application](element-application.md)</td>
<td><p>Represents an app that comprises part of or all of the functionality delivered in the package.</p></td>
</tr>
<tr class="odd">
<td>[Applications](element-applications.md)</td>
<td><p>Represents one or more apps that comprise the package.</p></td>
</tr>
<tr class="even">
<td>[Arguments](element-arguments.md)</td>
<td><p>Specifies the list of comma-separated arguments to pass to the executable.</p></td>
</tr>
<tr class="odd">
<td>[BackgroundTasks](element-backgroundtasks.md)</td>
<td><p>Defines an app extensibility point of type <strong>windows.backgroundTasks</strong>. Background tasks run in a dedicated background host; that is, without a UI.</p></td>
</tr>
<tr class="even">
<td>[Capabilities](element-capabilities.md)</td>
<td><p>Declares the access to protected user resources that the package requires.</p></td>
</tr>
<tr class="odd">
<td>[Capability](element-capability.md)</td>
<td><p>Declares a capability required by a package.</p></td>
</tr>
<tr class="even">
<td>[Certificate](element-certificate.md)</td>
<td><p>A certificate for use with the package and placed in the system certificate stores.</p></td>
</tr>
<tr class="odd">
<td>[Certificates](element-certificates.md)</td>
<td><p>Declares a package extensibility point of type <strong>windows.certificates</strong>. The app requires one or more certificates from the specified certificate stores.</p></td>
</tr>
<tr class="even">
<td>[Dependencies](element-dependencies.md)</td>
<td><p>Declares other packages that a package depends on to complete its software.</p></td>
</tr>
<tr class="odd">
<td>[Description](element-description.md)</td>
<td><p>A friendly description that can be displayed to users.</p></td>
</tr>
<tr class="even">
<td>[Device](element-device.md)</td>
<td><p>Declares a function for a device that is associated with the [<strong>DeviceCapability</strong>](element-devicecapability.md). On Windows 10.0.10240.0, a <strong>DeviceCapability</strong> can contain up to 100 <strong>Device</strong> elements. On Windows 10.0.10586.0, it can contain up to 1000 (for more details, see <strong>DeviceCapability</strong>).</p></td>
</tr>
<tr class="odd">
<td>[DeviceCapability](element-devicecapability.md)</td>
<td><p>Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 [<strong>Device</strong>](element-device.md) elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples).</p></td>
</tr>
<tr class="even">
<td>[DisplayName](element-displayname.md)</td>
<td><p>A friendly name that can be displayed to users.</p></td>
</tr>
<tr class="odd">
<td>[Extension (global)](element-1-extension.md)</td>
<td><p>Declares an extensibility point for the package.</p></td>
</tr>
<tr class="even">
<td>[Extension (in type: CT_PackageExtensions)](element-extension.md)</td>
<td><p>Declares an extensibility point for the package.</p></td>
</tr>
<tr class="odd">
<td>[Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md)</td>
<td><p>Defines one or more extensibility points for the app.</p></td>
</tr>
<tr class="even">
<td>[Extensions (type: CT_PackageExtensions)](element-extensions.md)</td>
<td><p>Defines one or more extensibility points for the package.</p></td>
</tr>
<tr class="odd">
<td>[Folder](element-folder.md)</td>
<td><p>Specifies a folder that the package shares with other packages from the same publisher.</p></td>
</tr>
<tr class="even">
<td>[Framework](element-framework.md)</td>
<td><p>Indicates whether the package is a framework package; that is, a package that can be used by other packages. Its value is <strong>false</strong> by default. You should not specify a value for it unless you are creating a framework.</p></td>
</tr>
<tr class="odd">
<td>[Function](element-function.md)</td>
<td><p>Declares the function for the device.</p></td>
</tr>
<tr class="even">
<td>[Identity](element-identity.md)</td>
<td><p>Defines a globally unique identifier for a package. A package identity is represented as a tuple of attributes of the package.</p></td>
</tr>
<tr class="odd">
<td>[InProcessServer](element-inprocessserver.md)</td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.inProcessServer</strong>. The app uses a dynamic link library (DLL) that exposes one or more activatable classes.</p></td>
</tr>
<tr class="even">
<td>[Instancing](element-instancing.md)</td>
<td><p>Specifies whether the executable runs as a single instance or can run as multiple instances.</p></td>
</tr>
<tr class="odd">
<td>[Interface](element-interface.md)</td>
<td><p>Declares an interface associated with the proxy.</p></td>
</tr>
<tr class="even">
<td>[Logo](element-logo.md)</td>
<td><p>A path to a file that contains an image.</p></td>
</tr>
<tr class="odd">
<td>[OutOfProcessServer](element-outofprocessserver.md)</td>
<td><p>Declares a package extension point of type <strong>windows.activatableClass.outOfProcessServer</strong>. The app uses an executable (EXE) that exposes one or more activatable classes.</p></td>
</tr>
<tr class="even">
<td>[Package](element-package.md)</td>
<td><p>Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
<tr class="odd">
<td>[PackageDependency](element-packagedependency.md)</td>
<td><p>Declares a dependency on another package that is marked as a framework package.</p></td>
</tr>
<tr class="even">
<td>[Path (type: ST_Executable)](element-1-path.md)</td>
<td><p>The path to the executable.</p></td>
</tr>
<tr class="odd">
<td>[Path (type: ST_FileName)](element-path.md)</td>
<td><p>The path to the DLL.</p></td>
</tr>
<tr class="even">
<td>[Properties](element-properties.md)</td>
<td><p>Defines additional metadata about the package including attributes that describe how the package appears to users.</p>
<div class="alert">
<strong>Note</strong>  You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely “|” and “all”, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](https://msdn.microsoft.com/library/windows/desktop/hh973484) if you get an error.
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td>[ProxyStub](element-proxystub.md)</td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.proxyStub</strong>. A proxy can be composed of one or more interfaces.</p></td>
</tr>
<tr class="even">
<td>[PublisherCacheFolders](element-publishercachefolders.md)</td>
<td><p>Declares a package extensibility point of type <strong>windows.publisherCacheFolders</strong>. This specifies one or more folders that the package shares with other packages from the same publisher.</p></td>
</tr>
<tr class="odd">
<td>[PublisherDisplayName](element-publisherdisplayname.md)</td>
<td><p>A friendly name for the publisher that can be displayed to users.</p></td>
</tr>
<tr class="even">
<td>[Resource](element-resource.md)</td>
<td><p>Declares a language for the resource contained in the package. The scale and DirectX feature level attributes are common for all resources in the package.</p></td>
</tr>
<tr class="odd">
<td>[ResourcePackage](element-resourcepackage.md)</td>
<td><p>Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is <strong>false</strong> by default. You should not specify a value for it unless you are creating a resource.</p></td>
</tr>
<tr class="even">
<td>[Resources](element-resources.md)</td>
<td><p>Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package.</p></td>
</tr>
<tr class="odd">
<td>[SelectionCriteria](element-selectioncriteria.md)</td>
<td><p>Defines selection criteria for the certificates defined for the package.</p></td>
</tr>
<tr class="even">
<td>[TargetDeviceFamily](element-targetdevicefamily.md)</td>
<td><p>Identifies the device family that your package targets. For more info about device families, see [Guide to UWP apps](https://msdn.microsoft.com/library/windows/apps/dn894631).</p></td>
</tr>
<tr class="odd">
<td>[Task](element-task.md)</td>
<td><p>The background task associated with the app extensibility point.</p></td>
</tr>
<tr class="even">
<td>[TrustFlags](element-trustflags.md)</td>
<td><p>Indicates whether the certificates for the package are exclusive to the package.</p></td>
</tr>
<tr class="odd">
<td>[pm:PhoneIdentity](element-pm-phoneidentity.md)</td>
<td><p>If your app is an update to an app previously made available on Windows Phone, ensure that this element matches what is in the app manifest of your previous app. Use the same GUIDs that were assigned to the app by the Store. This ensures that users of your app who are upgrading to Windows 10 will receive your new app as an update, and not as a duplicate.</p></td>
</tr>
<tr class="even">
<td>[uap:AppService](element-uap-appservice.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.appService</strong>. Application Contracts are a way for an app to invoke a background task belonging to another app; or for a background task invoked to service an app contract a way to communicate with its caller.</p></td>
</tr>
<tr class="odd">
<td>[uap:ApplicationContentUriRules](element-uap-applicationcontenturirules.md)</td>
<td><p>Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.</p></td>
</tr>
<tr class="even">
<td>[uap:AppointmentsProvider](element-uap-appointmentsprovider.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.appointmentsProvider</strong>.</p></td>
</tr>
<tr class="odd">
<td>[uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md)</td>
<td><p>Declares actions to take when a appointment is launched.</p></td>
</tr>
<tr class="even">
<td>[uap:AutoPlayContent](element-uap-autoplaycontent.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.autoPlayContent</strong>. The app provides the specified AutoPlay content actions.</p></td>
</tr>
<tr class="odd">
<td>[uap:AutoPlayDevice](element-uap-autoplaydevice.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.autoPlayDevice</strong>. The app provides the specified AutoPlay device actions.</p></td>
</tr>
<tr class="even">
<td>[uap:Capability](element-uap-capability.md)</td>
<td><p>Declares a capability required by a package.</p></td>
</tr>
<tr class="odd">
<td>[uap:Codec](element-uap-codec.md)</td>
<td><p>Specifies the codec to use for transcoding.</p></td>
</tr>
<tr class="even">
<td>[uap:DataFormat](element-uap-dataformat.md)</td>
<td><p>Specifies a data package format such as text or HTML format that the app can share. It is unique per application in the package and is case sensitive.</p></td>
</tr>
<tr class="odd">
<td>[uap:DefaultTile](element-uap-defaulttile.md)</td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
<tr class="even">
<td>[uap:DialProtocol](element-uap-dialprotocol.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.dialProtocol</strong>.</p></td>
</tr>
<tr class="odd">
<td>[uap:DisplayName](element-uap-displayname.md)</td>
<td><p>A friendly name that can be displayed to users.</p></td>
</tr>
<tr class="even">
<td>[uap:EditFlags](element-uap-editflags.md)</td>
<td><p>Specifies the type of info the user sees when opening a file associated to the extensibility point.</p></td>
</tr>
<tr class="odd">
<td>[uap:Extension](element-uap-extension.md)</td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
<tr class="even">
<td>[uap:FileOpenPicker](element-uap-fileopenpicker.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.fileOpenPicker</strong>. The app lets the user choose and open the specified types of files.</p></td>
</tr>
<tr class="odd">
<td>[uap:FileSavePicker](element-uap-filesavepicker.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.fileSavePicker</strong>. The app lets the user choose the file name, extension, and storage location for the specified types of files.</p></td>
</tr>
<tr class="even">
<td>[uap:FileType (in type: CT_FTASupportedFileTypes)](element-uap-filetype.md)</td>
<td><p>A supported file type specified as its file type extension.</p></td>
</tr>
<tr class="odd">
<td>[uap:FileType (type: ST_FileType)](element-1-uap-filetype.md)</td>
<td><p>A file type specified as its file type extension. It is unique per application in the package and is case sensitive.</p></td>
</tr>
<tr class="even">
<td>[uap:FileTypeAssociation](element-uap-filetypeassociation.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.fileTypeAssociation</strong>. A file type association indicates that the app is registered to handle files of the specified types.</p></td>
</tr>
<tr class="odd">
<td>[uap:InfoTip](element-uap-infotip.md)</td>
<td><p>Defines a string that provides additional info to the user about the file type.</p></td>
</tr>
<tr class="even">
<td>[uap:InitialRotationPreference](element-uap-initialrotationpreference.md)</td>
<td><p>Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate.</p>
<p>Note that on devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.</p>
<p>These orientation preference choices apply to both the [<strong>splash screen</strong>](https://msdn.microsoft.com/library/windows/apps/dn391687) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [<strong>AutoRotationPreferences</strong>](https://msdn.microsoft.com/library/windows/apps/dn264259) property.</p></td>
</tr>
<tr class="odd">
<td>[uap:LaunchAction (global)](element-2-uap-launchaction.md)</td>
<td><p>Describes an [<strong>uap:AppointmentsProviderLaunchActions</strong>](element-uap-appointmentsproviderlaunchactions.md) content action.</p></td>
</tr>
<tr class="even">
<td>[uap:LaunchAction (in type: CT_AutoPlayContent)](element-uap-launchaction.md)</td>
<td><p>Describes an AutoPlay content action.</p></td>
</tr>
<tr class="odd">
<td>[uap:LaunchAction (in type: CT_AutoPlayDevice)](element-1-uap-launchaction.md)</td>
<td><p>Describes an AutoPlay device action.</p></td>
</tr>
<tr class="even">
<td>[uap:LockScreen](element-uap-lockscreen.md)</td>
<td><p>Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked.</p></td>
</tr>
<tr class="odd">
<td>[uap:Logo](element-uap-logo.md)</td>
<td><p>A path to a file that contains an image.</p></td>
</tr>
<tr class="even">
<td>[uap:ManagedUrls](element-uap-managedurls.md)</td>
<td><p>Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies.</p></td>
</tr>
<tr class="odd">
<td>[uap:MediaPlayback](element-uap-mediaplayback.md)</td>
<td><p>Declares an app extensibility point of type <strong>mediaPlayback</strong> so that your app can declare that it performs video transcoding.</p></td>
</tr>
<tr class="even">
<td>[uap:Protocol](element-uap-protocol.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.protocol</strong>. A URI association indicates that the app is registered to handle URIs with the specified scheme.</p></td>
</tr>
<tr class="odd">
<td>[uap:Rotation](element-uap-rotation.md)</td>
<td><p>Specifies a single rotational orientation in which an app will display.</p></td>
</tr>
<tr class="even">
<td>[uap:Rule](element-uap-rule.md)</td>
<td><p>Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.</p></td>
</tr>
<tr class="odd">
<td>[uap:ShareTarget](element-uap-sharetarget.md)</td>
<td><p>Declares an app extension point of type <strong>windows.shareTarget</strong>. The app can share the specified types of files.</p></td>
</tr>
<tr class="even">
<td>[uap:ShowNameOnTiles](element-uap-shownameontiles.md)</td>
<td><p>Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.</p></td>
</tr>
<tr class="odd">
<td>[uap:ShowOn](element-uap-showon.md)</td>
<td><p>Describes whether Windows overlays the app’s name on top of the tile image that is shown on the Start screen.</p></td>
</tr>
<tr class="even">
<td>[uap:SplashScreen](element-uap-splashscreen.md)</td>
<td><p>Defines the appearance of the splash screen, which is displayed by the app during launch.</p></td>
</tr>
<tr class="odd">
<td>[uap:SupportedFileTypes (type: CT_CharmsSupportedFileTypes)](element-1-uap-supportedfiletypes.md)</td>
<td><p>Defines the file types that the app can share.</p></td>
</tr>
<tr class="even">
<td>[uap:SupportedFileTypes (type: CT_FTASupportedFileTypes)](element-uap-supportedfiletypes.md)</td>
<td><p>Defines the file types associated with the app. They are unique per package and are case sensitive.</p></td>
</tr>
<tr class="odd">
<td>[uap:SupportedUsers](element-uap-supportedusers.md)</td>
<td><p>Indicates whether or not the package is multi-user aware. This setting is used at install time to determine whether the package can be installed on the system.</p></td>
</tr>
<tr class="even">
<td>[uap:SupportsAnyFileType](element-uap-supportsanyfiletype.md)</td>
<td><p>Indicates whether all file types are supported for sharing.</p></td>
</tr>
<tr class="odd">
<td>[uap:Task](element-uap-task.md)</td>
<td><p>The background task associated with the app extensibility point.</p></td>
</tr>
<tr class="even">
<td>[uap:TileUpdate](element-uap-tileupdate.md)</td>
<td><p>Describes how the app tile receives update notifications.</p></td>
</tr>
<tr class="odd">
<td>[uap:Url](element-uap-url.md)</td>
<td><p>Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL.</p></td>
</tr>
<tr class="even">
<td>[uap:VisualElements](element-uap-visualelements.md)</td>
<td><p>Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
</tr>
<tr class="odd">
<td>[uap:VoipCall](element-uap-voipcall.md)</td>
<td><p>Declares an app extensibility point of type <strong>voipCall</strong> so that your app can declare that it can perform an upgrade from a cellular call to a VoIP video call, and/or whether it is a VoIP app that supports dialing phone numbers directly.</p></td>
</tr>
<tr class="even">
<td>[uap:VoipCallUpgrade](element-uap-voipcallupgrade.md)</td>
<td><p>Indicates that the app supports video upgrade. Video upgrade is a feature on some mobile devices such that, when a user is on a cellular call, the user can upgrade that call to a VoIP video call if there is an app installed that can service such a request. These upgrades can be non-seamless (we must drop the cellular call before starting the video call through the app) or seamless (the cellular call remains connected until the app tells us the video call is established).</p></td>
</tr>
<tr class="odd">
<td>[uap:VoipDialPhoneNumber](element-uap-voipdialphonenumber.md)</td>
<td><p>Indicates that the app supports dialing phone numbers.</p></td>
</tr>
<tr class="even">
<td>[uap:WebAccountProvider](element-uap-webaccountprovider.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.webAccountProvider</strong>.</p></td>
</tr>
</tbody>
</table>

 

 

 




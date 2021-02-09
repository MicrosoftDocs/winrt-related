---
description: Package manifest schema with Windows 8.1 minor extensions reference
Search.Product: eADQiWindows 10XVcnh
title: Windows 8.1 extensions manifest schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c

keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Windows 8.1 extensions manifest schema


This reference provides details for each element, attribute, and data type that defines the schema for the app package manifest for Windows 8.1 apps. The schema definition file is AppxManifestSchema2010_v2.xsd.

AppxManifestSchema2010_v2.xsd is the schema that defines the overall manifest schema for Windows 8.1 apps. AppxManifestSchema2010_v2.xsd is a copy of the Windows 8 manifest schema, AppxManifestSchema.xsd, but adds new elements and attributes in the Windows 8.1 namespace. This schema is only used to validate manifests that define OSMinVersion as 6.3.\*. These Windows 8.1 namespace types are imported into this schema from the AppxManifestSchema2013.xsd file.

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
<td><a href="element-activatableclass.md">ActivatableClass (type: CT_InProcessActivatableClass)</a> </td>
<td><p>Declares a runtime class associated with the extensibility point.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-activatableclass.md">ActivatableClass (type: CT_OutOfProcessActivatableClass)</a> </td>
<td><p>Declares a runtime class associated with the extensibility point.</p></td>
</tr>
<tr class="odd">
<td><a href="element-activatableclassattribute.md">ActivatableClassAttribute</a> </td>
<td><p>Defines an attribute of the class that is stored in the Windows Runtime property store.</p></td>
</tr>
<tr class="even">
<td><a href="element-application.md">Application</a> </td>
<td><p>Represents an app that comprises part of or all of the functionality delivered in the package.</p></td>
</tr>
<tr class="odd">
<td><a href="element-applicationcontenturirules.md">ApplicationContentUriRules</a> </td>
<td><p>Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.</p></td>
</tr>
<tr class="even">
<td><a href="element-applicationextensionchoice.md">ApplicationExtensionChoice</a> </td>
<td><p>The abstract application extension choice element for the XSD substitution group. This can't be declared in the XML.</p></td>
</tr>
<tr class="odd">
<td><a href="element-applications.md">Applications</a> </td>
<td><p>Represents one or more apps that comprise the package.</p></td>
</tr>
<tr class="even">
<td><a href="element-arguments.md">Arguments</a> </td>
<td><p>Specifies the list of comma-separated arguments to pass to the executable.</p></td>
</tr>
<tr class="odd">
<td><a href="element-autoplaycontent.md">AutoPlayContent</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.autoPlayContent</strong>. The app provides the specified AutoPlay content actions.</p></td>
</tr>
<tr class="even">
<td><a href="element-autoplaydevice.md">AutoPlayDevice</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.autoPlayDevice</strong>. The app provides the specified AutoPlay device actions.</p></td>
</tr>
<tr class="odd">
<td><a href="element-backgroundtasks.md">BackgroundTasks</a> </td>
<td><p>Defines an app extensibility point of type <strong>windows.backgroundTasks</strong>. Background tasks run in a dedicated background host; that is, without a UI.</p></td>
</tr>
<tr class="even">
<td><a href="element-capabilities.md">Capabilities</a> </td>
<td><p>Declares the access to protected user resources that the package requires.</p></td>
</tr>
<tr class="odd">
<td><a href="element-capability.md">Capability</a> </td>
<td><p>Declares a capability required by a package.</p></td>
</tr>
<tr class="even">
<td><a href="element-certificate.md">Certificate</a> </td>
<td><p>A certificate for use with the package and placed in the system certificate stores.</p></td>
</tr>
<tr class="odd">
<td><a href="element-certificates.md">Certificates</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.certificates</strong>. The app requires one or more certificates from the specified certificate stores.</p></td>
</tr>
<tr class="even">
<td><a href="element-dataformat.md">DataFormat</a> </td>
<td><p>Specifies a data package format such as text or HTML format that the app can share. It is unique per application in the package and is case sensitive.</p></td>
</tr>
<tr class="odd">
<td><a href="element-defaulttile.md">DefaultTile</a> </td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
<tr class="even">
<td><a href="element-dependencies.md">Dependencies</a> </td>
<td><p>Declares other packages that a package depends on to complete its software.</p></td>
</tr>
<tr class="odd">
<td><a href="element-description.md">Description</a> </td>
<td><p>A friendly description that can be displayed to users.</p></td>
</tr>
<tr class="even">
<td><a href="element-devicecapability.md">DeviceCapability</a> </td>
<td><p>Declares a device capability required by a package.</p></td>
</tr>
<tr class="odd">
<td><a href="element-devicecapabilitychoice.md">DeviceCapabilityChoice</a> </td>
<td><p>The abstract device capability choice element for the XSD substitution group. This can't be declared in the XML.</p></td>
</tr>
<tr class="even">
<td><a href="element-displayname.md">DisplayName</a> </td>
<td><p>A friendly name that can be displayed to users. This string is localizable.</p></td>
</tr>
<tr class="odd">
<td><a href="element-editflags.md">EditFlags</a> </td>
<td><p>Specifies the type of info the user sees when opening a file associated to the extensibility point.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-extension.md">Extension (in type: CT_PackageExtensions)</a> </td>
<td><p>Declares an extensibility point for the package.</p></td>
</tr>
<tr class="odd">
<td><a href="element-extension.md">Extension (type: CT_ApplicationExtension)</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-extensions.md">Extensions (type: CT_ApplicationExtensions)</a> </td>
<td><p>Defines one or more extensibility points for the app.</p></td>
</tr>
<tr class="odd">
<td><a href="element-extensions.md">Extensions (type: CT_PackageExtensions)</a> </td>
<td><p>Defines one or more extensibility points for the package.</p></td>
</tr>
<tr class="even">
<td><a href="element-fileopenpicker.md">FileOpenPicker</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileOpenPicker</strong>. The app lets the user choose and open the specified types of files.</p></td>
</tr>
<tr class="odd">
<td><a href="element-filesavepicker.md">FileSavePicker</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileSavePicker</strong>. The app lets the user choose the file name, extension, and storage location for the specified types of files.</p></td>
</tr>
<tr class="even">
<td><a href="element-filetype.md">FileType (in type: CT_FTASupportedFileTypes)</a> </td>
<td><p>A supported file type specified as its file type extension.</p></td>
</tr>
<tr class="odd">
<td><a href="element-1-filetype.md">FileType (type: ST_FileType)</a> </td>
<td><p>A file type specified as its file type extension. It is unique per application in the package and is case sensitive.</p></td>
</tr>
<tr class="even">
<td><a href="element-filetypeassociation.md">FileTypeAssociation</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileTypeAssociation</strong>. A file type association indicates that the app is registered to handle files of the specified types.</p></td>
</tr>
<tr class="odd">
<td><a href="element-framework.md">Framework</a> </td>
<td><p>Indicates whether the package is a framework package; that is, a package that can be used by other packages. Its value is <strong>false</strong> by default. You should not specify a value for it unless you are creating a framework.</p></td>
</tr>
<tr class="even">
<td><a href="element-identity.md">Identity</a> </td>
<td><p>Defines a globally unique identifier for a package. A package identity is represented as a tuple of attributes of the package.</p></td>
</tr>
<tr class="odd">
<td><a href="element-inprocessserver.md">InProcessServer</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.inProcessServer</strong>. The app uses a dynamic link library (DLL) that exposes one or more activatable classes.</p></td>
</tr>
<tr class="even">
<td><a href="element-infotip.md">InfoTip</a> </td>
<td><p>Defines a string that provides additional info to the user about the file type.</p></td>
</tr>
<tr class="odd">
<td><a href="element-initialrotationpreference.md">InitialRotationPreference</a> </td>
<td><p>Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate.</p>
<p>Note that on devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.</p>
<p>These orientation preference choices apply to both the [<strong>splash screen</strong>](element-splashscreen.md) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [<strong>AutoRotationPreferences</strong>](/uwp/api/Windows.Graphics.Display.DisplayInformation) property.</p></td>
</tr>
<tr class="even">
<td><a href="element-instancing.md">Instancing</a> </td>
<td><p>Specifies whether the executable runs as a single instance or can run as multiple instances.</p></td>
</tr>
<tr class="odd">
<td><a href="element-interface.md">Interface</a> </td>
<td><p>Declares an interface associated with the proxy.</p></td>
</tr>
<tr class="even">
<td><a href="element-launchaction.md">LaunchAction (in type: CT_AutoPlayContent)</a> </td>
<td><p>Describes an AutoPlay content action.</p></td>
</tr>
<tr class="odd">
<td><a href="element-1-launchaction.md">LaunchAction (in type: CT_AutoPlayDevice)</a> </td>
<td><p>Describes an AutoPlay device action.</p></td>
</tr>
<tr class="even">
<td><a href="element-lockscreen.md">LockScreen</a> </td>
<td><p>Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked.</p></td>
</tr>
<tr class="odd">
<td><a href="element-logo.md">Logo</a> </td>
<td><p>A path to a file that contains an image.</p></td>
</tr>
<tr class="even">
<td><a href="element-osmaxversiontested.md">OSMaxVersionTested</a> </td>
<td><p>This should be filled in by the developer with the highest version of Windows that the package was tested on. This field is required. Windows will not block installation of the package on versions of the OS higher than the value provided in this field. When an app is executed, Windows will compare this field to the actual OS version. If the value provided in this field is less than the current OS version, Windows may provide behavior compatible with the highest tested OS version for some or all APIs. If the value provided in this field is greater than or equal to the current OS version, Windows will not apply any compatibility changes to APIs.</p></td>
</tr>
<tr class="odd">
<td><a href="element-osminversion.md">OSMinVersion</a> </td>
<td><p>The minimum version of the operating system that the package requires.</p></td>
</tr>
<tr class="even">
<td><a href="element-outofprocessserver.md">OutOfProcessServer</a> </td>
<td><p>Declares a package extension point of type <strong>windows.activatableClass.outOfProcessServer</strong>. The app uses an executable (EXE) that exposes one or more activatable classes.</p></td>
</tr>
<tr class="odd">
<td><a href="element-package.md">Package</a> </td>
<td><p>Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
<tr class="even">
<td><a href="element-packagedependency.md">PackageDependency</a> </td>
<td><p>Declares a dependency on another package that is marked as a framework package.</p></td>
</tr>
<tr class="odd">
<td><a href="element-1-path.md">Path (type: ST_Executable)</a> </td>
<td><p>The path to the executable.</p></td>
</tr>
<tr class="even">
<td><a href="element-path.md">Path (type: ST_FileName)</a> </td>
<td><p>The path to the DLL.</p></td>
</tr>
<tr class="odd">
<td><a href="element-prerequisites.md">Prerequisites</a> </td>
<td><p>Declares the minimum operating system and software requirements that must exist for the package to be applicable to the system.</p></td>
</tr>
<tr class="even">
<td><a href="element-properties.md">Properties</a> </td>
<td><p>Defines additional metadata about the package including attributes that describe how the package appears to users.</p>
<div class="alert">
<strong>Note</strong>  You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely “|” and “all”, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td><a href="element-protocol.md">Protocol</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.protocol</strong>. A URI association indicates that the app is registered to handle URIs with the specified scheme.</p></td>
</tr>
<tr class="even">
<td><a href="element-proxystub.md">ProxyStub</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.proxyStub</strong>. A proxy can be composed of one or more interfaces.</p></td>
</tr>
<tr class="odd">
<td><a href="element-publisherdisplayname.md">PublisherDisplayName</a> </td>
<td><p>A friendly name for the publisher that can be displayed to users.</p></td>
</tr>
<tr class="even">
<td><a href="element-resource.md">Resource</a> </td>
<td><p>Declares a language for the resource contained in the package. The scale and DirectX feature level attributes are common for all resources in the package.</p></td>
</tr>
<tr class="odd">
<td><a href="element-resourcepackage.md">ResourcePackage</a> </td>
<td><p>Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is <strong>false</strong> by default. You should not specify a value for it unless you are creating a resource.</p></td>
</tr>
<tr class="even">
<td><a href="element-resources.md">Resources</a> </td>
<td><p>Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package.</p></td>
</tr>
<tr class="odd">
<td><a href="element-rotation.md">Rotation</a> </td>
<td><p>Specifies a single rotational orientation in which an app will display.</p></td>
</tr>
<tr class="even">
<td><a href="element-rule.md">Rule</a> </td>
<td><p>Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.</p></td>
</tr>
<tr class="odd">
<td><a href="element-selectioncriteria.md">SelectionCriteria</a> </td>
<td><p>Defines selection criteria for the certificates defined for the package.</p></td>
</tr>
<tr class="even">
<td><a href="element-sharetarget.md">ShareTarget</a> </td>
<td><p>Declares an app extension point of type <strong>windows.shareTarget</strong>. The app can share the specified types of files.</p></td>
</tr>
<tr class="odd">
<td><a href="element-splashscreen.md">SplashScreen</a> </td>
<td><p>Defines the appearance of the splash screen, which is displayed by the app during launch.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-supportedfiletypes.md">SupportedFileTypes (type: CT_CharmsSupportedFileTypes)</a> </td>
<td><p>Defines the file types that the app can share.</p></td>
</tr>
<tr class="odd">
<td><a href="element-supportedfiletypes.md">SupportedFileTypes (type: CT_FTASupportedFileTypes)</a> </td>
<td><p>Defines the file types associated with the app. They are unique per package and are case sensitive.</p></td>
</tr>
<tr class="even">
<td><a href="element-supportsanyfiletype.md">SupportsAnyFileType</a> </td>
<td><p>Indicates whether all file types are supported for sharing.</p></td>
</tr>
<tr class="odd">
<td><a href="element-task.md">Task</a> </td>
<td><p>The background task associated with the app extensibility point.</p></td>
</tr>
<tr class="even">
<td><a href="element-taskchoice.md">TaskChoice</a> </td>
<td><p>The abstract task choice element for the XSD substitution group. This can't be declared in the XML.</p></td>
</tr>
<tr class="odd">
<td><a href="element-trustflags.md">TrustFlags</a> </td>
<td><p>Indicates whether the certificates for the package are exclusive to the package.</p></td>
</tr>
<tr class="even">
<td><a href="element-visualelements.md">VisualElements</a> </td>
<td><p>Describes the visual aspects of the UWP app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
</tr>
<tr class="odd">
<td><a href="element-visualelementschoice.md">VisualElementsChoice</a> </td>
<td><p>The abstract visual elements choice element for the XSD substitution group. This can't be declared in the XML.</p></td>
</tr>
</tbody>
</table>

 

 

 

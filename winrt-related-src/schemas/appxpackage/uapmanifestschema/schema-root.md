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
ms.date: 04/10/2018
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
| [com:Aspect (in ExeServer/Class)](element-com-exe-aspect.md) | Specifies the desired data or view aspect of the object when drawing or getting data. |
| [com:Aspect (in SurrogateServer/Class)](element-com-surrogate-aspect.md) | Specifies the desired data or view aspect of the object when drawing or getting data. |
| [com:Class (in ExeServer)](element-com-exeserver-class.md) | Defines an ExeServer class registration. |
| [com:Class (in SurrogateServer/Class)](element-com-surrogateserver-class.md) | Defines a SurrogateServer class registration. |
| [com:ComInterface (in Application/Extensions)](element-com-interface.md) | Declares a package extension point of type windows.comInterface. The comInterface extension may include three types of registrations: Interface, ProxyStub, or TypeLib. |
| [com:ComInterface (in Package/Extensions)](element-com-package-interface.md) | Declares a package extension point of type windows.comInterface. The comInterface extension may include three types of registrations: Interface, ProxyStub, or TypeLib. |
| [com:ComServer](element-com-comserver.md) | Declares a package extension point of type windows.comServer. The comServer extension may include four types of registrations: ExeServer, SurrogateServer, ProgId, or TreatAsClass. |
| [com:Conversion (in ExeServer/Class)](element-com-exe-conversion.md) | Specifies the formats an application can read and write. |
| [com:Conversion (in SurrogateServer/Class)](element-com-surrogate-conversion.md) | Specifies the formats an application can read and write. |
| [com:DataFormat (in ExeServer/Class)](element-com-exe-dataformat.md) | The data format supported by an application. |
| [com:DataFormat (in SurrogateServer/Class)](element-com-surrogate-dataformat.md) | The data format supported by an application. |
| [com:DataFormats (in ExeServer/Class)](element-com-exe-dataformats.md) | Specifies the default and main data formats supported by an application. |
| [com:DataFormats (in SurrogateServer/Class)](element-com-surrogate-dataformats.md) | Specifies the default and main data formats supported by an application. |
| [com:DefaultIcon (in ExeServer/Class)](element-com-exe-defaulticon.md) | Provides default icon information for iconic presentations of objects. |
| [com:DefaultIcon (in SurrogateServer/Class)](element-com-surrogate-defaulticon.md) | Provides default icon information for iconic presentations of objects. |
| [com:ExeServer](element-com-exeserver.md) | Registers an ExeServer with one or many class registrations. |
| [com:Extension](element-com-extension.md) | Provides functionality to expose COM registrations to clients outside of the app package. |
| [com:Format (in ExeServer/Readable)](element-com-exe-rformat.md) | Specifies the file format an application can read (convert from). |
| [com:Format (in ExeServer/ReadWritable)](element-com-exe-rwformat.md) | Specifies the file format an application can read and write (activate as). |
| [com:Format (in SurrogateServer/Readable)](element-com-surrogate-rformat.md) | Specifies the file format an application can read (convert from). |
| [com:Format (in SurrogateServer/ReadWritable)](element-com-surrogate-rwformat.md) | Specifies the file format an application can read and write (activate as). |
| [com:ImplementedCategories (in ExeServer/Class)](element-com-exe-implementedcategories.md) | Specifies categories implemented by the class. |
| [com:ImplementedCategories (in SurrogateServer/Class)](element-com-surrogate-implementedcategories.md) | Specifies categories implemented by the class. |
| [com:ImplementedCategory (in ExeServer/Class)](element-com-exe-implementedcategory.md) | Indicates that the class has implemented the specified category. |
| [com:ImplementedCategory (in SurrogateServer/Class)](element-com-surrogate-implementedcategory.md) | Indicates that the class has implemented the specified category. |
| [com:Interface (in Application/Extensions)](element-com-interface.md) | Registers new COM Interfaces. |
| [com:Interface (in Package/Extensions)](element-com-package-cominterface.md) | Registers new COM Interfaces. |
| [com:MiscStatus (in ExeServer/Class)](element-com-exe-miscstatus.md) | Specifies how to create and display an object. |
| [com:MiscStatus (in SurrogateServer/Class)](element-com-surrogate-miscstatus.md) | Specifies how to create and display an object. |
| [com:ProgId](element-com-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique. |
| [com:ProxyStub (in ComInterface)](element-com-proxystub.md) | Registers a proxy stub. |
| [com:ProxyStub (in Package/Extensions)](element-com-package-proxystub.md) | Registers a proxy stub. |
| [com:Readable (in ExeServer)](element-com-exe-readable.md) | Specifies that an application can only read files. |
| [com:Readable (in SurrogateServer)](element-com-surrogate-readable.md) | Specifies that an application can only read files. |
| [com:ReadWritable (in ExeServer)](element-com-exe-ReadWritable.md) | Specifies that an application can read and write files. |
| [com:ReadWritable (in SurrogateServer)](element-com-surrogate-ReadWritable.md) | Specifies that an application can read and write files. |
| [com:SurrogateServer](element-com-surrogateserver.md) | Registers a SurrogateServer with one or many class registrations. |
| [com:ToolboxBitmap32 (in ExeServer/Class)](element-com-exe-toolboxbitmap32.md) | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. |
| [com:ToolboxBitmap32 (in SurrogateServer/Class)](element-com-surrogate-toolboxbitmap32.md) | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. |
| [com:TreatAsClass](element-com-treatasclass.md) | A registration that corresponds to a CLSID registration with the TreatAs subkey. |
| [com:TypeLib (in Package/Extensions)](element-com-package-interface-typelib.md) | A type library for an interface. |
| [com:TypeLib (in ComInterface)](element-com-typelib.md) | Registers a type library. |
| [com:TypeLib (in Package/Extensions)](element-com-package-typelib.md) | Registers a type library. |
| [com:Verb (in ExeServer/Class)](element-com-exe-verb.md) | The verb to be registered for an application. |
| [com:Verb (in SurrogateServer/Class)](element-com-surrogate-verb.md) | The verb to be registered for an application. |
| [com:Verbs (in ExeServer/Class)](element-com-exe-verbs.md) | Specifies the verbs to be registered for an application. |
| [com:Verbs (in SurrogateServer/Class)](element-com-surrogate-verbs.md) | Specifies the verbs to be registered for an application. |
| [com:Version (in ComInterface/TypeLib)](element-com-version.md) | Version number and additional information about the type library. |
| [com:Version (in Package/Extensions)](element-com-package-version.md) | Version number and additional information about the type library. |
| [com:Win32Path (in ComInterface/TypeLib)](element-com-win32path.md) | A path to the 32-bit type library. |
| [com:Win32Path (in Package/Extensions)](element-com-package-win32path.md) | A path to the 32-bit type library. |
| [com:Win64Path (in ComInterface/TypeLib)](element-com-win64path.md) | A path to the 64-bit type library. |
| [com:Win64Path (in Package/Extensions)](element-com-package-win64path.md) | A path to the 64-bit type library. |
| [com2:ProxyStubDll](element-com2-proxystubdll.md) | Specifies the path and processor architecture of a ProxyStub DLL. |
| [com2:ProxyStubDll (in Package/Extensions)](element-com2-package-proxystubdll.md) | Specifies the path and processor architecture of a ProxyStub DLL. |
| [Dependencies](element-dependencies.md) | Declares other packages that a package depends on to complete its software. |
| [Description](element-description.md) | A friendly description that can be displayed to users. |
| [desktop2:AppPrinter](element-desktop2-appprinter.md) | Enables the ability to install software file printers in Windows Desktop Bridge apps. |
| [desktop2:DesktopEventLogging](element-desktop2-desktopeventlogging.md) | Enables Windows Desktop Bridge apps to register for Windows event logging. |
| [desktop2:DesktopPreviewHandler](element-desktop2-desktoppreviewhandler.md) | Enables declaration of a preview handler for a file type association. |
| [desktop2:DesktopPropertyHandler](element-desktop2-DesktopPropertyHandler.md) | Enables declaration of a property handler for a file type association. |
| [desktop2:EventMessageFiles](element-desktop2-EventMessageFiles.md) | Contains event message files. |
| [desktop2:Extension (in Application/Extensions)](element-desktop2-Extension.md) | Declares an extensibility point for the app. |
| [desktop2:Extension (in Package/Extensions)](element-desktop2-package-extension.md) | Declares an extensibility point for the app. |
| [desktop2:File](element-desktop2-file.md) | Specifies the path to an event message file. |
| [desktop2:FilterExtension](element-desktop2-FilterExtension.md) | Specifies the file type to be registered by the app. |
| [desktop2:FirewallRules](element-desktop2-FirewallRules.md) | Specifies firewall exception rules used by Windows Desktop Bridge apps. |
| [desktop2:OleClass](element-desktop2-OleClass.md) | Enables OLE to get the OLE class registered for a given file extension. |
| [desktop2:Rule](element-desktop2-rule.md) | Defines a firewall exception rule. |
| [desktop2:SearchFilterHandler](element-desktop2-SearchFilterHandler.md) | Enables Windows Desktop Bridge apps to register IFilters to extract file properties for searching. |
| [desktop2:SearchPropertyHandler](element-desktop2-SearchPropertyHandler.md) | Enables Windows Desktop Bridge apps to install property handlers on your system. These handlers are used to read properties from files for indexing and search. |
| [desktop2:ThumbnailHandler](element-desktop2-ThumbnailHandler.md) | Enables a ThumbnailProvider for a file type association. |
| [desktop2:TypesSupported](element-desktop2-TypesSupported.md) | Contains the event log types that are supported. |
| [desktop2:TypeSupported](element-desktop2-TypeSupported.md) | Specifies the types of events that are supported. |
| [desktop3:AutoPlayHandler](element-desktop3-AutoPlayHandler.md) | Handler for AutoPlay, which can present your app as an option when a user connects a device to their PC. |
| [desktop3:BannersHandler](element-desktop3-BannersHandler.md) | Registration of a Windows Shell BannersHandler for cloud based placeholder files. |
| [desktop3:CloudFiles](element-desktop3-CloudFiles.md) | Registration for the handlers implemented in an application and context menu options for cloud based placeholder files. |
| [desktop3:CloudFilesContextMenus](element-desktop3-CloudFilesContextMenus.md) | Registration of a context menu for a cloud based placeholder file. |
| [desktop3:Content](element-desktop3-content.md) | Defines the content information of an AutoPlayHandler. |
| [desktop3:CustomStateHandler](element-desktop3-CustomStateHandler.md) | Registration of a Windows Shell CustomStateHandler for cloud based placeholder files. |
| [desktop3:Device](element-desktop3-Device.md) | Defines the device information of an AutoPlayHandler. |
| [desktop3:ExtendedPropertyHandler](element-desktop3-ExtendedPropertyHandler.md) | Registration of a Windows Shell ExtendedPropertyHandler for cloud based placeholder files. |
| [desktop3:InvokeAction](element-desktop3-InvokeAction.md) | Contains content and device information for invoking an AutoPlay action. |
| [desktop3:PropertyList](element-desktop3-PropertyList.md) | Contains the properties that are under the Properties tab of a file. |
| [desktop3:PropertyLists](element-desktop3-PropertyLists.md) | Contains a list of properties to show under the properties tab of a file. |
| [desktop3:ThumbnailProviderHandler](element-desktop3-ThumbnailProviderHandler.md) | Registration of a Windows Shell ThumbnailProviderHandler for cloud based placeholder files. |
| [desktop3:Verb](element-desktop3-Verb.md) | Specifies the names of items in the File Explorer context menu for cloud based placeholder files. |
| [desktop4:ContentUriSource](element-desktop4-ContentUriSource.md) | Registration of a Windows Shell ContentUriSource enabling cloud storage providers to provide a file ID for a given local path. |
| [desktop4:DesktopIconOverlayHandler](element-desktop4-DesktopIconOverlayHandler.md) | Windows Shell icon overlay handlers for cloud based placeholder files. |
| [desktop4:DesktopIconOverlayHandlers](element-desktop4-DesktopIconOverlayHandlers.md) | Contains Windows Shell icon overlay handlers for cloud based placeholder files. |
| [desktop4:Extension](element-desktop4-Extension.md) | Declares an extensibility point for the app. |
| [desktop4:FileExplorerContextMenus](element-desktop4-FileExplorerContextMenus.md) | Registers items for the context menu of File Explorer. |
| [desktop4:ItemType](element-desktop4-ItemType.md) | Contains the type of command to be registered in the context menu. |
| [desktop4:Verb](element-desktop4-verb.md) | Names and class IDs of the commands registered in the Shell for a file explorer context menu. |
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
| [pm:PhoneIdentity](element-pm-phoneidentity.md) | If your app is an update to an app previously made available on Windows Phone, ensure that this element matches what is in the app manifest of your previous app. Use the same GUIDs that were assigned to the app by the Store. This ensures that users of your app who are upgrading to Windows 10 will receive your new app as an update, and not as a duplicate. |
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. **Note:**  You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely “&#124;” and “all”, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](https://msdn.microsoft.com/library/windows/desktop/hh973484) if you get an error. |
| [ProxyStub](element-proxystub.md) | Declares a package extensibility point of type **windows.activatableClass.proxyStub**. A proxy can be composed of one or more interfaces. |
| [PublisherCacheFolders](element-publishercachefolders.md) | Declares a package extensibility point of type **windows.publisherCacheFolders**. This specifies one or more folders that the package shares with other packages from the same publisher. |
| [PublisherDisplayName](element-publisherdisplayname.md) | A friendly name for the publisher that can be displayed to users. |
| [rescap2:Extension](element-rescap2-extension-manual.md) | Declares an extensibility point for the app. |
| [rescap3:DesktopApp](element-rescap3-desktopapp.md) | Specifies information for redirecting a Windows Desktop Bridge app's tiles and pins. |
| [rescap3:DesktopAppMigration](element-rescap3-desktopappmigration.md) | Specifies where to redirect user tiles and pins to a Windows Desktop Bridge app. |
| [rescap3:Extension](element-rescap3-extension.md) | Declares an extensibility point for the app. |
| [rescap3:MigrationProgId (in uap:Extension)](element-rescap3-migrationprogid.md) | Contains a migration Prog Id string for protocols and file type associations. |
| [rescap3:MigrationProgId (in uap:Protocol)](element-uap-protocol-migrationprogids.md) | Contains a migration Prog Id string for protocols and file type associations. |
| [rescap3:MigrationProgIds (in uap:Extension)](element-rescap3-migrationprogids.md) | Contains Migration Prog Ids for protocols and file type associations. |
| [rescap3:MigrationProgIds (in uap:Protocol)](element-uap-protocol-migrationprogids.md) | Contains Migration Prog Ids for protocols and file type associations. |
| [rescap4:ClassicAppCompatKey](element-rescap4-ClassicAppCompatKey.md) | Registry keys for discovering classic app installations and launching executables. |
| [rescap4:ClassicAppCompatKeys](element-rescap4-ClassicAppCompatKeys.md) | Contains registry keys for discovering classic app installations and launching executables. |
| [rescap4:Extension](element-rescap4-extension.md) | Declares an extensibility point for the app. |
| [Resource](element-resource.md) | Declares a language for the resource contained in the package. The scale and DirectX feature level attributes are common for all resources in the package. |
| [ResourcePackage](element-resourcepackage.md) | Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a resource. |
| [Resources](element-resources.md) | Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package. |
| [SelectionCriteria](element-selectioncriteria.md) | Defines selection criteria for the certificates defined for the package. |
| [serverpreview:Attribute](element-serverpreview-attribute-manual.md) | Represents an attiribute that should be added to or modified in the applicationHost.config file. |
| [serverpreview:CollectionElement](element-serverpreview-collectionelement-manual.md) | Represents a collection element with the specified attributes that should be added to the applicationHost.config file. |
| [serverpreview:EventProvider](element-serverpreview-eventprovider-manual.md) | Identifies an event tracing extension to add to the server-specific app extensions. |
| [serverpreview:EventProviders](element-serverpreview-eventproviders-manual.md) | Declares an app extensibility point of type **windows.eventProviders**. This element identifies one or more event tracing extensions to add to the server-specific app extensions. |
| [serverpreview:Extension](element-serverpreview-extension-manual.md) | Declares an extensibility point for the app. |
| [serverpreview:IisModule](element-serverpreview-iismodule-manual.md) | Identifies an Internet Information Service (IIS) module to install, update, or uninstall out-of-band on Nano Server. |
| [serverpreview:IisModules](element-serverpreview-iismodules-manual.md) | Declares an app extensibility point of type **windows.iisModules**. This element identifies one or more Internet Information Service (IIS) modules to install, update, or uninstall out-of-band on Nano Server. |
| [serverpreview:Mof](element-serverpreview-mof-manual.md) | Specifies the Managed Object Format (MOF) files to use to install or uninstall the Windows Management Instrumentation (WMI) provider. |
| [serverpreview:NTService](element-serverpreview-ntservice-manual.md) | Identifies an NT Service to install, update, or uninstall on Nano Server. |
| [serverpreview:NTServices](element-serverpreview-ntservices-manual.md) | Declares an app extensibility point of type **windows.ntServices**. This element identifies one or more NT Services to install, update, or uninstall on Nano Server. |
| [serverpreview:PerformanceProvider](element-serverpreview-performanceprovider-manual.md) | Identifies a performance counter to add to the server-specific app extensions. |
| [serverpreview:PerformanceProviders](element-serverpreview-performanceproviders-manual.md) | Declares an app extensibility point of type **windows.performanceProviders**. This element identifies one or more performance counters to add to the server-specific app extensions. |
| [serverpreview:SectionData](element-serverpreview-sectiondata-manual.md) | Identifies section data that will be embedded into applicationHost.config file of an IIS installation. Each SectionData element specifies one combination of a section and a path as determined by the attributes of the element. |
| [serverpreview:SectionDefinition](element-serverpreview-sectiondefinition-manual.md) | Identifies an Internet Information Service (IIS) SectionDefinition as it pertains to a same-named XML element in an applicationHost.config file. |
| [serverpreview:SectionGroupDefinition](element-serverpreview-sectiongroupdefinition-manual.md) | Identifies an Internet Information Service (IIS) SectionGroupDefinition as it pertains to a same-named XML element in an applicationHost.config file. |
| [serverpreview:ServiceDependencies](element-serverpreview-servicedependencies-manual.md) | Specifies the set of additional services on which the service that corresponds to the parent serverpreview:NTService element depends. |
| [serverpreview:ServiceDependency](element-serverpreview-servicedependency-manual.md) | Specifies an additional service on which the service that corresponds to the grandparent serverpreview:NTService element depends. |
| [serverpreview:ServiceParameterDword](element-serverpreview-serviceparameterdword-manual.md) | Specifies the value of a parameter for the service that has a data type of REG_DWORD. This parameter corresponds to a registry value that is created under the HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\ServiceName\Parameters key or specified subkey. |
| [serverpreview:ServiceParameterKey](element-serverpreview-serviceparameterkey-manual.md) | Specifies a parameter for the service. This parameter corresponds to a registry subkey that is created under the HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\ServiceName\Parameters key. |
| [serverpreview:ServiceParameters](element-serverpreview-serviceparameters-manual.md) | Specifies a set of parameters to configure for the service. These parameters correspond to registry values that are created under the HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\ServiceName\Parameters key. |
| [serverpreview:ServiceParameterString](element-serverpreview-serviceparameterstring-manual.md) | Specifies the value of a parameter for the service that has a data type of REG_SZ. This parameter corresponds to a registry value that is created under the HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\ServiceName\Parameters key or specified subkey. |
| [serverpreview:WmiProvider](element-serverpreview-wmiprovider-manual.md) | Identifies a Windows Management Instrumentation (WMI) provider to install, update, or uninstall out-of-band on Nano Server. |
| [serverpreview:WmiProviders](element-serverpreview-wmiproviders-manual.md) | Declares an app extensibility point of type windows.wmiProviders. This element identifies one or more Windows Management Instrumentation (WMI) providers to install, update, or uninstall out-of-band on Nano Server. |
| [TargetDeviceFamily](element-targetdevicefamily.md) | Identifies the device family that your package targets. For more info about device families, see [Guide to UWP apps](https://msdn.microsoft.com/library/windows/apps/dn894631). |
| [Task](element-task.md) | The background task associated with the app extensibility point. |
| [TypeLib (in ComInterface/Interface)](element-com-interface-typelib.md) | A type library for an interface. |
| [TrustFlags](element-trustflags.md) | Indicates whether the certificates for the package are exclusive to the package. |
| [uap:ApplicationContentUriRules](element-uap-applicationcontenturirules.md) | Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard. |
| [uap:AppointmentsProvider](element-uap-appointmentsprovider.md) | Declares an app extensibility point of type **windows.appointmentsProvider**. |
| [uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md) | Declares actions to take when a appointment is launched. |
| [uap:AppService](element-uap-appservice.md) | Declares an app extensibility point of type **windows.appService**. Application Contracts are a way for an app to invoke a background task belonging to another app; or for a background task invoked to service an app contract a way to communicate with its caller. |
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
| [uap2:SupportedVerbs](element-uap2-supportedverbs.md) | Contains verbs for a file context menu. |
| [uap2:Verb](element-uap2-verb.md) | Defines the verbs associated with a file context menu and enables Windows Desktop Bridge apps to use ddeexec to launch. |
| [uap3:AppExtension](element-uap3-appextension-manual.md) | Declares an app extensibility point of type **windows.appExtension**. This element indicates which categories of extensions the app intends to consume and/or host. |
| [uap3:AppExtensionHost](element-uap3-appextensionhost-manual.md) | Declares an app extensibility point of type **windows.appExtensionHost**. This element indicates which categories of extensions the app can host.
 |
| [uap3:AppointmentDataProvider](element-uap3-appointmentdataprovider-manual.md) | Declares an app extensibility point of type **windows.appointmentDataProvider**. This element enables apps to become data providers for appointments. |
| [uap3:AppService](element-uap3-appservice-manual.md) | Declares an app extensibility point of type **windows.appService**. Application Contracts are a way for an app to invoke a background task belonging to another app, or for a background task invoked to service an app contract a way to communicate with its caller. |
| [uap3:AppUriHandler](element-uap3-appurihandler-manual.md) | Declares an app extensibility point of type **windows.appUriHandler**. |
| [uap3:Capability](element-uap3-capability-manual.md) | Declares a capability required by a package. |
| [uap3:ContactDataProvider](element-uap3-contactdataprovider-manual.md) | Declares an app extensibility point of type **windows.contactDataProvider**. This element enables apps to become data providers for contacts. |
| [uap3:EmailDataProvider](element-uap3-emaildataprovider-manual.md) | Declares an app extensibility point of type **windows.emailDataProvider**. This element enables apps to become data providers for email. |
| [uap3:Extension](element-uap3-extension-manual.md) | Declares an extensibility point for the app. |
| [uap3:Host](element-uap3-host-manual.md) | Represents a valid HTTP or HTTPS host name that the app wants to register as able to handle. |
| [uap3:MainPackageDependency](element-uap3-mainpackagedependency-manual.md) | Specifies the main app package to which this supplemental package applies. |
| [uap3:Name](elemennt-uap3-name-manual.md) | Specifies a category of extensions that the app can host. |
| [uap3:Properties](elemnt-uap3-properties-manual.md) | Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system. The information is only read by the host app. |
| [uap3:VisualElements](element-uap3-visualelements-manual.md) | Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance. |
| [uap4:ContactPanel](element-uap4-contactpanel.md) | Enables the contacts panel in a Windows app. |
| [uap4:CustomCapability](element-uap4-customcapability.md) | Declares a custom capability required by a package. |
| [uap4:DevicePortalProvider](element-uap4-deviceportalprovider.md) | Defines a Device Portal provider for deployment. |
| [uap4:Extension](element-uap4-extension.md) | Declares an extensibility point for the app. |
| [uap4:Font](element-uap4-font.md) | Specifies the font file packaged with the app. |
| [uap4:InputType](element-uap4-inputtype.md) | The media codec input type. |
| [uap4:InputTypes](element-uap4-inputtypes.md) | Contains the media codec input types. |
| [uap4:Kind](element-uap4-kind.md) | Specifies the Kind value. |
| [uap4:KindMap](element-uap4-kindmap.md) | Specifies what Kind is and how it's used. |
| [uap4:LoopbackAccessRules](element-uap4-loopbackaccessrules.md) | Contains rules for a loopback filter that enables communication between an app and a service. |
| [uap4:MediaCodec](element-uap4-mediacodec.md) | Defines an extension that enables an app to install media codecs from the Microsoft Store. |
| [uap4:MediaEncodingProperties](element-uap4-mediaencodingproperties.md) | Contains the media coded input and output types. |
| [uap4:OutputType](element-uap4-outputtype.md) | The media codec output type. |
| [uap4:OutputTypes](element-uap4-outputtypes.md) | Contains the media codec output types. |
| [uap4:Rule](element-uap4-rule.md) | Defines rules for inbound and outbound loopback connections. |
| [uap4:SharedFonts](element-uap4-sharedfonts.md) | Contains the locations of shared fonts to be used with the app. |
| [uap5:ActivatableClass](element-uap5-ActivatableClass.md) | Declares a runtime class associated with the extensibility point. |
| [uap5:ActivatableClassAttribute](element-uap5-ActivatableClassAttribute.md) | Defines an attribute of the class that is stored in the Windows Runtime property store. |
| [uap5:AppExecutionAlias](element-uap5-AppExecutionAlias.md) | Specifies the application's execution alias to determine the executable of the app to be activated. |
| [uap5:Arguments](element-uap5-Arguments.md) | Specifies the list of comma-separated arguments to pass to the executable. |
| [uap5:ContentType](element-uap5-ContentType.md) | Specifies the media/content type supported by the media source. |
| [uap5:DriverConstraint](element-uap5-DriverConstraint.md) | Specifies the details of a driver paired with a UWP app. |
| [uap5:DriverDependency](element-uap5-DriverDependency.md) | Contains the driver constraint information for a UWP app. If `DriverDependency` is used, the specified driver must be present for the app to load. |
| [uap5:ExecutionAlias](element-uap5-ExecutionAlias.md) | The executable of a UWP app to be activated from a command prompt. |
| [uap5:Extension](element-uap5-Extension.md) | Declares an extensibility point for the app. |
| [uap5:FileType](element-uap5-FileType.md) | Specifies the file type supported by the media source. |
| [uap5:Host](element-uap5-Host.md) | Represents a valid HTTP or HTTPS host name with a wildcard that the app wants to register as able to handle. |
| [uap5:InputType](element-uap5-InputType.md) | Specifies media input sub-types. |
| [uap5:InputTypes](element-uap5-InputTypes.md) | Contains a list of media input sub-types. |
| [uap5:Instancing](element-uap5-Instancing.md) | Specifies whether the executable runs as a single instance or can run as multiple instances. |
| [uap5:MediaSource](element-uap5-MediaSource.md) | Specifies the media source and the app service that it exposes. |
| [uap5:MixedRealityModel](element-uap5-MixedRealityModel.md) | An element used to define a 3D model as the default representation of an app. When launched from a virtual or mixed reality device, this model will represent the app in the virtual setting. |
| [uap5:OutOfProcessServer](element-uap5-OutOfProcessServer.md) | Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. This enables 3rd party WinRT classes defined in the app package to be called from a Win32 process. |
| [uap5:Path](element-uap5-Path.md) | The path to the executable. |
| [uap5:StartupTask](element-uap5-StartupTask.md) | Specifies a startup task for your application. |
| [uap5:SupportedContentTypes](element-uap5-SupportedContentTypes.md) | Contains the media/content types supported by the media source. |
| [uap5:SupportedFileTypes](element-uap5-SupportedFileTypes.md) | Contains the file types supported by the media source. |
| [uap5:UserActivity](element-uap5-UserActivity.md) | Allows an app to opt out of engagement data tracking. |
| [uap5:VideoRendererEffect](element-uap5-VideoRendererEffect.md) | Enables activation of video renderer effects in apps. |
| [uap5:VideoRendererExtensionProfile](element-uap5-VideoRendererExtensionProfile.md) | Specifies a video renderer profile. |
| [uap5:VideoRendererExtensionProfiles](element-uap5-VideoRendererExtensionProfiles.md) | Contains a list of video renderer profiles. |
| [uap6:AllowExecution](element-uap6-AllowExecution.md) | Indicates whether the contents of the package will be allowed to execute. |
| [uap6:BarcodeScannerProvider](element-uap6-BarcodeScannerProvider.md) | Used for enabling the support of a barcode scanner. |
| [uap6:Capability](element-uap6-capability.md) | Declares a capability required by a package. |
| [uap6:Extension](element-uap6-Extension.md) | Declares an extensibility point for the app. |
| [uap6:LoaderSearchPathEntry](element-uap6-LoaderSearchPathEntry.md) | A path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes. |
| [uap6:LoaderSearchPathOverride](element-uap6-LoaderSearchPathOverride.md) | An extension that allows an app developer to declare a path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes. |
| [uap6:LocalExperiencePack](element-uap6-LocalExperiencePack.md) | This extension provides a means to deliver translated app resources. |
| [uap6:SpatialBoundingBox](element-uap6-SpatialBoundingBox.md) | Used to define the center point and the extents for a bounding volume. |
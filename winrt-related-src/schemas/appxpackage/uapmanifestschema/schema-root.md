---
description: Provides details for each element, attribute, and data type that defines the schema for the app package manifest for Windows 10 apps.
Search.Product: eADQiWindows 10XVcnh
title: Package manifest schema reference for Windows 10
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
keywords: windows 10, uwp, schema, package manifest
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
| [com2:ComInterface](element-com2-cominterface.md) | Declares a package extension point of type windows.comInterface. The comInterface extension may include three types of registrations: Interface, ProxyStub, or TypeLib.  |
| [com2:ComServer](element-com2-comserver.md) | Declares a package extension point of type windows.comServer. The comServer extension may include a ServiceServer registration.  |
| [com2:Extension](element-com2-extension.md) | Provides functionality to expose COM registrations to clients outside of the app package.  |
| [com2:ProxyStubDll](element-com2-proxystubdll.md) | Specifies the path and processor architecture of a ProxyStub DLL. |
| [com2:ProxyStubDll (in Package/Extensions)](element-com2-package-proxystubdll.md) | Specifies the path and processor architecture of a ProxyStub DLL. |
| [com3:Class](element-com3-class.md) | DDefines a class registration in a COM server hosted in a Windows service that is registered in a [com3:ServiceServer](element-com3-serviceserver.md) element.    |
| [com3:ExeServer](element-com3-exeserver.md) |Registers an ExeServer with one or many class registrations.   |
| [com3:ProgId](element-com3-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID for a com3:ServiceServer class registration. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique.    |
| [com3:ServiceServer](element-com3-serviceserver.md) | Registers a COM server (with one or more class registrations) hosted in a Windows service that is declared with a corresponding [desktop6:Service](element-desktop6-service.md) element.   |
| [com3:SurrogateServer](element-com3-surrogateserver.md) | Registers a SurrogateServer with one or many class registrations.   |
| [com3:TreatAsClass](element-com3-treatasclass.md) | A registration that corresponds to a CLSID registration with the TreatAs subkey for a com3:ServiceServer class.    |
| [Dependencies](element-dependencies.md) | Declares other packages that a package depends on to complete its software. |
| [Description](element-description.md) | A friendly description that can be displayed to users. |
| [desktop:ExecutionAlias](element-desktop-executionalias.md) | The executable of a UWP app to be activated from a command prompt. |
| [desktop:Extension](element-desktop-extension.md) | Declares an extensibility point for the app. |
| [desktop:FullTrustProcess](element-desktop-fulltrustprocess.md) | Represents a desktop process that runs in full-trust. |
| [desktop:SearchProtocolHandler](element-desktop-searchprotocolhandler.md) | Represents a desktop process handles the search protocol for the app. |
| [desktop:StartupTasks](element-desktop-startuptasks.md) | Represents a desktop process that runs during app startup. |
| [desktop:ToastNotificationActivation](element-desktop-toastnotificationactivation.md) | Allows toast notification to be received within the app. |
| [desktop2:AppPrinter](element-desktop2-appprinter.md) | Enables the ability to install software file printers in Windows Desktop Bridge apps. |
| [desktop2:DesktopEventLogging](element-desktop2-desktopeventlogging.md) | Enables Windows Desktop Bridge apps to register for Windows event logging. |
| [desktop2:DesktopPreviewHandler](element-desktop2-desktoppreviewhandler.md) | Enables declaration of a preview handler for a file type association. |
| [desktop2:DesktopPropertyHandler](element-desktop2-DesktopPropertyHandler.md) | Enables declaration of a property handler for a file type association. |
| [desktop2:EventMessageFiles](element-desktop2-EventMessageFiles.md) | Contains event message files. |
| [desktop:Extension (in Application/Extensions)](element-desktop-extension.md) | Declares an extensibility point for the app. |
| [desktop:FullTrustProcess](element-desktop-fulltrustprocess.md) | Represents a desktop process that runs in full-trust. |
| [desktop:ParameterGroup](element-desktop-parametergroup.md) | Represents a group of command-line parameters for a full-trust process. |
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
| [desktop5:ItemType](element-desktop5-itemtype.md) | Contains the type of command to be registered in the context menu. |
| [desktop5:Verb](element-desktop5-verb.md) | Names and class IDs of the commands registered in the Shell for a file explorer context menu. |
| [desktop6:BinaryData](element-desktop6-binarydata.md) | Specifies binary data for a trigger event of a service. |
| [desktop6:CustomInstall](element-desktop6-custominstall.md) | Enables your desktop application to specify one or more additional installer files (.exe or .msi) that are installed with your desktop application.  |
| [desktop6:DataItem](element-desktop6-dataitem.md) | Specifies a string value for a trigger event of a service. |
| [desktop6:Dependencies](element-desktop6-dependencies.md) | Specifies one or more dependent services for the current service. |
| [desktop6:DependentService](element-desktop6-dependentservice.md) | Specifies a dependent service for the current service. |
| [desktop6:Extension (child of Application)](element-desktop6-extension.md) | Declares an extensibility point for the app. |
| [desktop6:Extension (child of Package)](element-desktop6-package-extension.md) | Declares an extensibility point for the app. |
| [desktop6:FileSystemWriteVirtualization](element-desktop6-filesystemwritevirtualization.md) | Indicates whether virtualization for the file system is enabled for your desktop application. |
| [desktop6:InstallActions](element-desktop6-installactions.md) | Specifies installer files (.exe or .msi) that are run before the first launch of your desktop application. This element is currently intended to be used only by desktop PC games that are packaged in an MSIXVC container. |
| [desktop6:InstallAction](element-desktop6-installaction.md) | Specifies an installer file (.exe or .msi) that is run before the first launch of your desktop application. This element is currently intended to be used only by desktop PC games that are packaged in an MSIXVC container. |
| [desktop6:RegistryWriteVirtualization](element-desktop6-extension.md) | Indicates whether virtualization for the registry is enabled for your desktop application. |
| [desktop6:KeywordAnyData](element-desktop6-keywordanydata.md) | Specifies a 64-bit unsigned integer value for a trigger event of a service. |
| [desktop6:KeywordAllData](element-desktop6-keywordalldata.md) | Specifies a 64-bit unsigned integer value for a trigger event of a service. |
| [desktop6:MutablePackageDirectories](element-desktop6-mutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods). |
| [desktop6:MutablePackageDirectory](element-desktop6-mutablepackagedirectory.md) | Specifies a folder under the %ProgramFiles%\ModifiableWindowsApps path where the contents of your desktop application's install folder are projected so that users can modify the installation files (for example, to install mods). |
| [desktop6:LevelData](element-desktop6-leveldata.md) | Specifies a byte value for a trigger event of a service. |
| [desktop6:RepairActions](element-desktop6-repairactions.md) | Specifies installer files (.exe or .msi) that are run when the user selects the repair or reset options in the Settings page for your desktop application. This element is currently intended to be used only by desktop PC games that are packaged in an MSIXVC container.  |
| [desktop6:RepairAction](element-desktop6-repairaction.md) | Specifies an installer file (.exe or .msi) that is run when the user selects the repair or reset options in the Settings page for your desktop application. This element is currently intended to be used only by desktop PC games that are packaged in an MSIXVC container. |
| [desktop6:Service](element-desktop6-service.md) | Specifies a service that is installed and registered along with the app. These services can be configured to run under either the Local Service, Network Service or Local System account. |
| [desktop6:StringData](element-desktop6-stringdata.md) | Specifies one or more string data values for a trigger event of a service. |
| [desktop6:TriggerEvents](element-desktop6-triggerevents.md) | Describes one or more trigger events for the current service. |
| [desktop6:TriggerCustom](element-desktop6-triggercustom.md) | Describes a trigger event for the current service. |
| [desktop6:UninstallActions](element-desktop6-uninstallactions.md) | Specifies installer files (.exe or .msi) that are run when the user uninstalls your desktop application. This element is currently intended to be used only by desktop PC games that are packaged in an MSIXVC container. |
| [desktop6:UninstallAction](element-desktop6-uninstallaction.md) | Specifies an installer file (.exe or .msi) that is run when the user uninstalls your desktop application. This element is currently intended to be used only by desktop PC games that are packaged in an MSIXVC container.  |
| [desktop7:ApplicationRegistration](element-desktop7-applicationregistration.md)| Registers an application, replacing the need to register the application in the system PATH variable. |
| [desktop7:AppMigration](element-desktop7-appmigration.md)| Specifies the target of a deactivated shortcut that should be updated as part of the migration of a recently uninstalled app.|
| [desktop7:AppMigrations](element-desktop7-appmigrations.md)| Specifies a set of app migration entries for a deactivated shortcut for a recently uninstalled app.|
| [desktop7:ApprovedShellExtension](element-desktop7-approvedshellextension.md)| Specifies that a shell extension should be added to the approved shell extensions list when installed. |
| [desktop7:ControlPanelItem](element-desktop7-controlpanelitem.md)| Registers an extension as a control panel item.|
| [desktop7:DefaultIcon](element-desktop7-defaulticon.md)| Specifies the icon to show for this item in the Control Panel.|
| [desktop7:DesktopApp](element-desktop7-desktopapp.md)| Specifies the source and target for a tile or pin that should be updated as part of a desktop app migration.|
| [desktop7:DesktopAppMigration](element-desktop7-desktopappmigration.md)| Specifies a set of app migration entries for tiles and pins.|
| [desktop7:ErrorReporting](element-desktop7-errorreporting.md)| Specifies a set of runtime exception helper modules.|
| [desktop7:Extension (child of Application)](element-desktop7-extension.md)| Declares an extensibility point for the app (in Package/Applications; desktop7:Extension).|
| [desktop7:Extension (child of Package)](element-desktop7-package-extension.md)| Declares an extensibility point for the app (in Package/Extensions; desktop7:Extension).|
| [desktop7:InfoTip](element-desktop7-infotip.md)| Specifies the Infotip string to show when the mouse hovers over the item’s icon.|
| [desktop7:LocalizedString](element-desktop7-localizedstring.md)| Specifies the localized string to show for this item in the Control Panel.|
| [desktop7:MailProvider](element-desktop7-mailprovider.md)| Registers a dll as a mail provider.|
| [desktop7:RuntimeExceptionHelperModule](element-desktop7-runtimeexceptionhelpermodule.md)| Specifies a module that will be launched in the event of a runtime exception.|
| [desktop7:Service](element-desktop7-service.md)| Specifies a service that is installed and registered along with the app. These services can be configured to run under either the Local Service, Network Service or Local System account.|
| [desktop7:ShadowCopyExcludeFile](element-desktop7-shadowcopyexcludefile.md)| Specifies a file to be excluded by the Volume Shadow Copy Service (VSS).|
| [desktop7:ShadowCopyExcludeFiles](element-desktop7-shadowcopyexcludefiles.md)| Specifies a set of files to be excluded by the Volume Shadow Copy Service (VSS).|
| [desktop7:Shortcut](element-desktop7-shortcut.md)| Creates a shortcut to a file.|
| [desktop7:SystemFileAssociation](element-desktop7-systemfileassociation.md)| Registers system file associations for an app. |
| [desktop8:Channels](element-desktop8-channels.md) | Allows one or more channels to be specified for event tracing. |
| [desktop8:Channel](element-desktop8-channel.md) | Specifies a channel to be used for event tracing. |
| [desktop8:EventTracing](element-desktop8-eventtracing.md) | Enables your desktop application to log application-defined events to be consumed in real time or saved to a log file. |
| [desktop8:Extension](element-desktop8-extension.md) | Declares an extensibility point for the app. |
| [desktop8:ImportChannel](element-desktop8-importchannel.md) | Specifies an imported channel to be used for event tracing. |
| [desktop8:Logging](element-desktop8-logging.md) | Provides access to the Logging feature within an Event Tracing channel. |
| [desktop8:MutablePackageDirectories](element-desktop8-mutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where you can modify the installation files for your application. |
| [desktop8:MutablePackageDirectory](element-desktop8-mutablepackagedirectory.md) | Registers a provider to Event Tracing and enables its functionality. |
| [desktop8:Provider](element-desktop8-provider.md) | Registers a provider to Event Tracing and enables its functionality. |
| [desktop8:Publishing](element-desktop8-publishing.md) | Provides access to the Publishing feature within an Event Tracing channel. | 
| [desktop8:UserMutablePackageDirectories](element-desktop8-usermutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods). |
| [desktop8:UserMutablePackageDirectory](element-desktop8-usermutablepackagedirectory.md) | Enables your desktop application to specify a folder where users can modify the installation files for your application (for example, to install mods). |
| [desktop9:ExtensionHandler](element-desktop9-extensionhandler.md) | Specifies a handler for a legacy [IContextMenu](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) implementation of a context menu handler shell extension for a packaged desktop app.  |
| [desktop9:FileExplorerClassicContextMenuHandler](element-desktop9-fileexplorerclassiccontextmenuhandler.md) | Registers a legacy [IContextMenu](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) implementation of a context menu handler shell extension for a packaged desktop app.  |
| [desktop9:FileExplorerClassicDragDropContextMenuHandler](element-desktop9-fileexplorerclassicdragdropcontextmenuhandler.md) | Registers a legacy [IContextMenu](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) implementation of a drag and drop handler shell extension for a packaged desktop app.  |
| [desktop10:CustomDesktopEventLog](element-desktop10-customdesktopeventlog.md) | efines a custom event log.  |
| [desktop10:CustomEventSource](element-desktop10-customeventsource.md) | Defines an event source within a custom event log.  |
| [desktop10:DataShortcut](element-desktop10-datashortcut.md) | Creates a shortcut to a file that is not an executable.  |
| [desktop10:DataShortcuts](element-desktop10-datashortcuts.md) | Specifies a list of non-executable shortcuts.  |
| [desktop10:EventMessageFiles](element-desktop10-eventmessagefiles.md) | Defines 1 or more DLL files containing the language strings describing the events.  |
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app (in Package/Extensions; desktop10:Extension).  |
| [desktop10:File](element-desktop10-file.md) | Defines an event log DLL within the package.  |
| [desktop10:Folder](element-desktop10-folder.md) | Defines a folder to hold shortcuts, with localizable details.  |
| [desktop10:IconHandler](element-desktop10-iconhandler.md) | Enables an IconHandler for a file type association.  |
| [desktop10:PredefinedTriggerEvents](element-desktop10-predefinedtriggerevents.md) | Describes predefined trigger events for the current service.  |
| [desktop10:SupportedProtocol](element-desktop10-supportedprotocol.md) | Specifies a URL protocol scheme.  |
| [desktop10:SupportedProtocols](element-desktop10-supportedprotocols.md) | DSpecifies the supported URL protocol schemes for a given key.  |
| [desktop10:TypesSupported](element-desktop10-typessupported.md) | Defines 1 or more of the event log types supported by the event source.  |
| [desktop10:TypeSupported](element-desktop10-typesupported.md) | Specifies a supported event log type.  |
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
| [mp:PhoneIdentity](element-mp-phoneidentity.md) | If your app is an update to an app previously made available on Windows Phone, ensure that this element matches what is in the app manifest of your previous app. Use the same GUIDs that were assigned to the app by the Store. This ensures that users of your app who are upgrading to Windows 10 will receive your new app as an update, and not as a duplicate. |
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. **Note:**  You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely “&#124;” and “all”, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error. |
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
| [rescap4:PrimaryInteropAssemblies](element-rescap4-primaryInteropAssemblies.md) | Defines package assembly configuration. |
| [rescap4:Redirect](element-rescap4-redirect.md) | Specifies redirect information for interop assemblies. |
| [Resource](element-resource.md) | Declares a language for the resource contained in the package. The scale and DirectX feature level attributes are common for all resources in the package. |
| [ResourcePackage](element-resourcepackage.md) | Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a resource. |
| [Resources](element-resources.md) | Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package. |
| [SelectionCriteria](element-selectioncriteria.md) | Defines selection criteria for the certificates defined for the package. |
| [TargetDeviceFamily](element-targetdevicefamily.md) | Identifies the device family that your package targets. For more info about device families, see [Guide to UWP apps](/windows/uwp/get-started/universal-application-platform-guide). |
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
| [uap2:Extension](element-uap2-extension.md) | Declares an extensibility point for the app. |
| [uap2:ManagedUrls](element-uap2-managedurls.md) | Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies. |
| [uap2:SupportedVerbs](element-uap2-supportedverbs.md) | Contains verbs for a file context menu. |
| [uap2:Url](element-uap2-url.md) | Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL. |
| [uap2:Verb](element-uap2-verb.md) | Defines the verbs associated with a file context menu and enables Windows Desktop Bridge apps to use ddeexec to launch. |
| [uap2:WebAccountProvider](element-uap2-webaccountprovider.md) | Declares an app extensibility point of type windows.webAccountProvider. |
| [uap3:AppExecutionAlias](element-uap3-appexecutionalias.md) | Specifies the application's execution alias to determine the executable of the app to be activated. |
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
| [uap3:FileTypeAssociations](element-uap3-filetypeassociations.md) | Defines the types of files used within the application. |
| [uap3:Host](element-uap3-host-manual.md) | Represents a valid HTTP or HTTPS host name that the app wants to register as able to handle. |
| [uap3:MainPackageDependency](element-uap3-mainpackagedependency-manual.md) | Specifies the main app package to which this supplemental package applies. |
| [uap3:Name](elemennt-uap3-name-manual.md) | Specifies a category of extensions that the app can host. |
| [uap3:Properties](elemnt-uap3-properties-manual.md) | Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system. The information is only read by the host app. |
| [uap3:Protocol](element-uap3-protocol.md) | Declares an app extensibility point of type windows.protocol. |
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
| [uap6:Extension (in Application/Extensions)](element-uap6-Extension.md) | Declares an extensibility point for the app. |
| [uap6:Extension (in Package/Extensions)](element-uap6-package-extension.md) | Declares an extensibility point for the app. |
| [uap6:LoaderSearchPathEntry](element-uap6-LoaderSearchPathEntry.md) | A path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes. |
| [uap6:LoaderSearchPathOverride](element-uap6-LoaderSearchPathOverride.md) | An extension that allows an app developer to declare a path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes. |
| [uap6:LocalExperiencePack](element-uap6-LocalExperiencePack.md) | This extension provides a means to deliver translated app resources. |
| [uap6:SpatialBoundingBox](element-uap6-SpatialBoundingBox.md) | Used to define the center point and the extents for a bounding volume. |
| [uap7:Capability](element-uap7-capability.md) | Declares a capability required by a package. |
| [uap7:EnterpriseDataProtection](element-uap7-enterprisedataprotection.md) | Declares that the app is safe for auto-encryption and allows it to be managed without device enrollment via Windows Information Protection policy. |
| [uap7:Extension](element-uap7-extension.md) | Declares an extensibility point for the app. |
| [uap7:ImportRedirectionTable](element-uap7-ImportRedirectionTable.md) | Allows for a packaged app to declare API redirections. |
| [uap7:OSPackageDependency](element-uap7-ospackagedependency.md) | Defines a package dependency for a UWP app. |
| [uap7:Properties](element-uap7-properties.md) | Properties of an application. |
| [uap7:SharedFonts](element-uap7-sharedfonts.md) | Contains the locations of shared fonts to be used with the app. |
| [uap8:PosPaymentConnector](element-uap8-posPaymentConnector.md) | Contains device information for Point-of-Sale/Point-of-Service devices. |
| [uap8:DataProtection](element-uap8-dataProtection.md) | Settings to configure data encryption. |
| [uap8:ExecutionAlias](element-uap8-executionalias.md) | The executable of a UWP app to be activated from a command prompt. |
| [uap10:AllowExternalContent](element-uap10-allowexternalcontent.md) | Enables your package manifest to reference content outside the package, in a specific location on disk, for [sparse package](/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps) scenarios. |
| [uap10:Content](element-uap10-content.md) | Indicates whether Windows will enforce run time package integrity checks on the entire contents of the package. |
| [uap10:DisplayName](element-uap10-displayname.md) | A friendly name that can be displayed to users. |
| [uap10:Extension (Child of Application)](element-uap10-extension.md) | Declares an extensibility point for the app. |
| [uap10:Extension (Child of Package)](element-uap10-package-extension.md) | Declares an extensibility point for the app. |
| [uap10:HostRuntime](element-uap10-hostruntime.md) | Defines a package-wide extension that defines the runtime information to be used when activating a hosted app. |
| [uap10:HostRuntimeDependency](element-uap10-hostruntimedependency.md) | Defines a dependency on a host app package for the current app package. |
| [uap10:InstalledLocationVirtualization](element-uap10-installedlocationvirtualization.md) | Defines an extension for a desktop app in an MSIX package that redirects any writes to the app's installation directory to a location in the [app data](/windows/uwp/design/app-settings/store-and-retrieve-app-data). |
|
| [uap10:Logo](element-uap10-logo.md) | A path to a file that contains an image. |
| [uap10:MediaContentDecryptionModule](element-uap10-mediacontentdecryptionmodule.md) | Defines an extension for a desktop app in an MSIX package that defines decryption information to be used to access media files.
| [uap10:PackageIntegrity](element-uap10-packageintegrity.md) | Specifies the level of run time package integrity checks and remediation for the package.  |
| [uap10:Protocol](element-uap10-protocol.md) | Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme. |
| [uap10:UpdateActions](element-uap10-UpdateActions.md) | Specifies what happens during app updates to files in the app's installation directory that were previously modified, added, or deleted by the app. This element is intended to be used in conjunction with the [uap10:InstalledLocationVirtualization](element-uap10-installedlocationvirtualization.md) extension. |
| [uap12:Extension](element-uap12-extension.md) | Declares an extensibility point for the app. |
| [uap12:Host](element-uap12-host.md) | Declares domain and subdomain parameters for the uap12 extension. |
| [uap13:AppInstaller](element-uap13-appinstaller.md) | Specifies a directory containing the installation files for the app. |
| [uap13:AutoUpdate](element-uap13-autoupdate.md) | Specifies automatic update configuration for the app. |
| [uap13:Extension](element-uap13-extension.md) | Declares an extensibility point for the app. |
| [uap13:HostRuntimeDependency](element-uap13-hostruntimedependency.md) | Declares publisher information for the app. |
| [virtualization:ExcludedDirectories](element-virtualization-excludeddirectories.md) | Specifies the list of directories that are excluded from file system virtualization. |
| [virtualization:ExcludedDirectory](element-virtualization-excludeddirectory.md) | Specifies a directory that is excluded from file system virtualization. |
| [virtualization:ExcludedKey](element-virtualization-excludedkey.md) | Specifies a key that is excluded from registry key virtualization. |
| [virtualization:ExcludedKeys](element-virtualization-excludedkeys.md) | Specifies the list of keys that are excluded from registry virtualization. |
| [virtualization:FileSystemWriteVirtualization](element-virtualization-filesystemwritevirtualization.md) | Indicates whether virtualization for the file system is enabled for a package. |
| [virtualization:RegistryWriteVirtualization](element-virtualization-registrywritevirtualization.md) | Indicates whether virtualization for the registry is enabled for a package. |
| [win32dependencies:ExternalDependency](element-win32dependencies-externaldependency.md) | Specifies an external dependency that is not included in the MSIX but will be chain installed as part of the app installation. |
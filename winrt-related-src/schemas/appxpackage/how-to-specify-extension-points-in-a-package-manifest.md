---
description: To declare an extensibility point for your app, use the Extension (CT\_ApplicationExtensions) element. To declare an extensibility point for the package, use the Extension (CT\_PackageExtensions) element.
Search.Product: eADQiWindows 10XVcnh
title: How to specify extensions in a package manifest
ms.assetid: 0c781926-91a9-4daf-b59b-ad9bd4ea71c8


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# How to specify extensions in a package manifest


**Note**  For Windows 10, see [What's different in Windows 10.](uapmanifestschema/what-s-changed-in-windows-10.md)

 

Your app can use extensibility points to interact with the system or other apps. To declare an extensibility point for your app, use the [**Extension (CT\_ApplicationExtensions)**](./appxmanifestschema/element-1-extension.md) element. To declare an extensibility point for the package, use the [**Extension (CT\_PackageExtensions)**](./appxmanifestschema/element-extension.md) element.

Alternatively, you can package your app using Visual Studio. See [Packaging your app using Visual Studio](/windows/uwp/packaging/). Note that in Microsoft Visual Studio they are called “Declarations” and there is no distinction between package and app level extensions.

## Instructions

### Step 1:

Follow the steps in [How to create a basic package manifest](how-to-create-a-basic-package-manifest.md).

### Step 2:

If the extensibility point is a package extensibility point, add a [**Package/Extensions**](./appxmanifestschema/element-extensions.md) node. The schema for each extensibility point is category-specific. For more info, see the description of the **Category** attribute for the [**Extension (CT\_PackageExtensions)**](./appxmanifestschema/element-extension.md) element.

Here's an example **Package/Extensions** node. Both extensions are **windows.activatableClass** extensions.

**Note**  The category name and child element names are related. In this example **Category** value ends with inProcessServer and child element is InProcessServer (different casing though).

 

```XML
<Package xmlns="http://schemas.microsoft.com/appx/2010/manifest">
   <Extensions>
      <Extension Category="windows.activatableClass.inProcessServer">
         <InProcessServer>
            <Path>bin\GrayscaleTransform.dll</Path>
            <ActivatableClass ActivatableClassId="Microsoft.Samples.GrayscaleEffect" ThreadingModel="both" />
         </InProcessServer>
      </Extension>
   </Extensions>
</Package>
```

### Step 3:

If the extensibility point is an app extensibility point, add a [**Package/Applications/Application/Extensions**](./appxmanifestschema/element-1-extensions.md) node. The schema for each extensibility point is category-specific. For more info, see the description of the **Category** attribute for the [**Extension (CT\_ApplicationExtensions)**](./appxmanifestschema/element-1-extension.md) element.

Here's an example **Package/Applications/Application/Extensions** node. The extensions is a **windows.fileTypeAssociation** extension. Some extensions contain child elements like in the example below and others do not, like **windows.accountPictureProvider**.

**Note**  The category name and child element names are related. In this example **Category** value ends with fileTypeAssociation and child element is FileTypeAssociation (different casing though).

 

```XML
<Package xmlns="http://schemas.microsoft.com/appx/2010/manifest">
   <Applications>
      <Application Id="AssociationLaunching.App">
         <Extensions>
            <Extension Category="windows.fileTypeAssociation">
               <FileTypeAssociation Name="imagetypes">
                  <SupportedFileTypes>
                     <FileType>.gif</FileType>
                     <FileType>.jpg</FileType>
                     <FileType>.png</FileType>
                  </SupportedFileTypes>
               </FileTypeAssociation>
            </Extension>
            <Extension Category=”windows.accountPictureProvider”/>
         </Extensions>
      </Application>
   </Applications>
</Package>
```

## Related topics


[How to create a package manifest manually](how-to-create-a-package-manifest-manually.md)

 

 

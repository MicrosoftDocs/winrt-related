---
description: To package your app, you must create a package manifest that contains the elements that are required by that the package manifest schema.
Search.Product: eADQiWindows 10XVcnh
title: How to create a basic package manifest for Windows 8
ms.assetid: f91fe2f6-4c9c-4965-8c35-8c02b0c66bd0


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# How to create a basic package manifest for Windows 8


**Note**  For Windows 10, see [What's different in Windows 10.](uapmanifestschema/what-s-changed-in-windows-10.md)

 

To package your app, you must create a package manifest that contains the elements that are required by that the package manifest schema.

Alternatively, you can package your app using Visual Studio. See [Packaging your app using Visual Studio](/windows/uwp/packaging/).

## Instructions

### Step 1: Create the .appxmanifest File

Using a text editor, create a file (which will contain XML) and name it Package.appxmanifest.

### Step 2: Add the basic template

Add this template to your Package.appxmanifest file.

```XML
<?xml version="1.0" encoding="utf-8"?>
<Package xmlns="http://schemas.microsoft.com/appx/2010/manifest">
  <Identity Name="" 
            Version="" 
            Publisher="" />
  <Properties>
    <DisplayName></DisplayName>
    <PublisherDisplayName></PublisherDisplayName>
    <Logo></Logo>
  </Properties>
  <Prerequisites>
    <OSMinVersion></OSMinVersion>
    <OSMaxVersionTested></OSMaxVersionTested>
  </Prerequisites>
  <Resources>
    <Resource Language="" />
  </Resources>
  <Applications>
    <Application Id="" StartPage="">
      <VisualElements DisplayName="" Description=""
           Logo="" SmallLogo=""  
           ForegroundText="" BackgroundColor="">
         <SplashScreen Image="" />
      </VisualElements>
    </Application>
  </Applications>
</Package>
```

The next steps show you how to fill in the elements and attributes that are required to complete the template.

### Step 3: Add the identity info

The [**Identity**](appxmanifestschema/element-identity.md) element has 3 required attributes. Here's an example **Identity** element with placeholder text for the attributes. The values of the **Name** attribute and the **Publisher** attribute (the values of **CN**, **O**, **L**, **S**, and **C**) in the example below are provided by the store, for apps which are uploaded to the store.

```XML
<Identity Name="MyCompany.MySuite.MyApp" 
          Version="1.0.0.0" 
          Publisher="CN=MyCompany, O=MyCompany, L=MyCity, S=MyState, C=MyCountry"/>
```

### Step 4: Add the package properties

The [**Properties**](appxmanifestschema/element-properties.md) element has 3 required child elements. Here is an example **Properties** node with placeholder text for the elements. The **DisplayName** is the name of your app that you reserve in the store, for apps which are uploaded to the store.

```XML
<Properties>
  <DisplayName>MyApp</DisplayName>
  <PublisherDisplayName>MyCompany</PublisherDisplayName>
  <Logo>images\icon.png</Logo>
</Properties>
```

### Step 5: Add the prerequisites

Here is an example [**Prerequisites**](appxmanifestschema/element-prerequisites.md) node.

```XML
<Prerequisites>
  <OSMinVersion>6.2.1</OSMinVersion>
  <OSMaxVersionTested>6.2.1</OSMaxVersionTested>
</Prerequisites>
```

### Step 6: Add the resources

Here is an example [**Resources**](appxmanifestschema/element-resources.md) node.

```XML
<Resources>
  <Resource Language="en-us" />
</Resources>
```

### Step 7: Add the optional info

You can use the [**Applications**](appxmanifestschema/element-applications.md) element to specify one or more apps for the package. Note that although each package can contain one or more apps, packages that contain multiple apps won't pass the Microsoft Store certification process.

The entry for an app must specify certain attributes of the [**VisualElements**](appxmanifestschema/element-visualelements.md) element and a [**SplashScreen**](appxmanifestschema/element-splashscreen.md) element. This entry can also specify a [**DefaultTile**](appxmanifestschema/element-defaulttile.md) element. Here is an example [**Applications**](appxmanifestschema/element-applications.md) node with placeholder text.

```XML
<Applications>
  <Application Id="MyApp" StartPage="default.html">
    <VisualElements DisplayName="My App" Description="A useful description." 
         Logo="images\icon.png" SmallLogo="images\small_icon.png" 
         ForegroundText="dark" BackgroundColor="#FFFFFF" >
      <SplashScreen Image="images\splash.png" />
    </VisualElements>
  </Application>
</Applications>
```

## Related topics


[How to create a package manifest manually](how-to-create-a-package-manifest-manually.md)

 

 

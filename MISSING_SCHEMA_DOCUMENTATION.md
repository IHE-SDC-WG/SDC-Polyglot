# Missing SDC Schema Documentation

This document identifies elements and attributes defined in the SDC schema files that are **not documented** in `Schema/SDCSchema.ipynb`.

## Summary

- **Total schema elements**: 320
- **Total schema attributes**: 319  
- **Elements documented**: 57 (18%)
- **Attributes documented**: 31 (10%)
- **Missing elements**: 272 (85%)
- **Missing attributes**: 288 (90%)

## Critical Missing Elements

These are core SDC elements that should be documented:

### Form Design & Structure
- `DataElement` - Root element for Data Elements (separate from FormDesign)
- `DemogFormDesign` - Root element for demographic forms (mentioned but not fully explained)
- `Header` - Header section (mentioned but not documented)
- `Footer` - Footer section (mentioned but not documented)
- `Rules` - Rules element for form logic

### Events & Actions
- `BeforeLoadForm` - Event fired before form loads
- `BeforeLoadData` - Event fired before data loads
- `BeforeShowForm` - Event fired before form displays
- `BeforeDataSubmit` - Event fired before data submission
- `BeforeCloseForm` - Event fired before form closes
- `OnEvent` - Generic event handler
- `OnClick` - Click event handler
- `OnEnter` - Enter event handler
- `OnExit` - Exit event handler
- `OnSelect` - Selection event handler
- `OnDeselect` - Deselection event handler
- `AfterChange` - Change event handler

### Actions & Rules
- `Action` / `Actions` - Action elements for form behavior
- `ActivateIf` - Conditional activation guard
- `DeActivateIf` - Conditional deactivation guard
- `SelectIf` - Conditional selection guard
- `DeselectIf` - Conditional deselection guard
- `CallFunction` - Function call action
- `CallBoolFunction` - Boolean function call
- `SetValue` - Set value action
- `SetAttributeValue` - Set attribute action

### Response & Data Types
- `ResponseValue` - Response value element
- `TypedValue` - Strongly-typed value (mentioned but not fully explained)
- All the various datatype elements (string, integer, date, etc. - some mentioned but not comprehensively)

### List & Selection
- `ListHeaderText` - Header text for lists
- `LookupEndPoint` - Web service endpoint for dynamic lists
- `ListItemMatchTargets` - List item matching targets
- `IllegalCoSelectedListItems` - Illegal co-selection rules
- `IllegalListItemPairings` - Illegal pairing rules

### Links & Resources
- `Link` - Link element (mentioned but not fully documented)
- `LinkText` - Link text
- `LinkURI` - Link URI
- `BlobContent` - Binary large object content
- `BinaryMediaBase64` - Base64-encoded binary media
- `BlobURI` - URI to blob resource
- `Hash` - Hash value for blobs

### Coding & Terminology
- `CodedValue` - Coded value element (mentioned but not fully documented)
- `Code` - Code element
- `CodeText` - Code text
- `CodeURI` - Code URI
- `CodeSystem` - Code system information
- `CodeSystemName` - Code system name
- `CodeSystemURI` - Code system URI
- `OID` - Object identifier
- `Version` - Version information
- `ReleaseDate` - Release date

### Contacts & Organizations
- `Contact` / `Contacts` - Contact information
- `Person` - Person information
- `PersonName` - Person name
- `Organization` - Organization information
- `OrgName` - Organization name
- `Email` - Email address
- `Phone` - Phone number
- `StreetAddress` - Street address
- `WebURL` - Web URL

### Inject Form
- `InjectForm` - Form injection element (mentioned but not documented)
- `InjectionSourceURI` - Source URI for injection

### Button Actions
- `ButtonAction` - Button action element (mentioned but not documented)

### Properties & Metadata
- `Description` - Description element
- `Documentation` - Documentation element
- `RichText` - Rich text element

### Package & Template Admin
- `SDCPackage` - SDC Package element
- `TemplateAdmin` - Template administration
- `Admin` - Administration metadata
- `FormPackageGroup` - Form package group
- `MainFormPackage` - Main form package
- `DemogFormPackage` - Demographic form package
- `InjectedFormPackage` - Injected form package

### Mapping
- `Map` - Mapping element
- `ItemMap` - Item mapping
- `MappedCode` - Mapped code
- `DefaultCodeSystem` - Default code system

## Critical Missing Attributes

### FormDesign Attributes
- `versionPrev` - Previous version identifier
- `instanceID` - Instance identifier
- `instanceVersion` - Instance version
- `instanceVersionPrev` - Previous instance version
- `instanceVersionURI` - Instance version URI (mentioned but not fully explained)
- `formInstanceURI` - Form instance URI (mentioned but not fully explained)
- `formInstanceVersionURI` - Form instance version URI (mentioned but not fully explained)
- `formPreviousInstanceVersionURI` - Previous form instance version URI (mentioned but not fully explained)

### Question & ListItem Attributes
- `selectionActivatesItems` - Items to activate on selection
- `selectionSelectsListItems` - List items to select on selection
- `associatedValue` - Associated value for list item
- `associatedValueType` - Type of associated value
- `mustImplement` - Whether element must be implemented (mentioned but not fully explained)

### Response Field Attributes
- `responseRequired` - Whether response is required (mentioned but not fully explained)
- `defaultListItemDataType` - Default data type for list items

### ListField Attributes
- `colTextDelimiter` - Column text delimiter
- `minSelections` - Minimum number of selections
- `ordered` - Whether list is ordered
- `sorted` - Whether list is sorted
- `sortDirection` - Sort direction

### InjectForm Attributes
- `InjectionSourceURI` - Source URI for injection
- `rootItemID` - Root item ID for injection
- `serverURI` - Server URI

### Display & Behavior Attributes
- `readOnly` - Read-only flag (mentioned but not fully explained)
- `visible` - Visibility flag
- `enabled` - Enabled flag
- `isActive` - Active status
- `isEnabled` - Enabled status
- `isReadOnly` - Read-only status
- `isRequired` - Required status
- `isSelected` - Selected status
- `isVisible` - Visible status

### Data Type Attributes
- `allowGT`, `allowGTE`, `allowLT`, `allowLTE` - Comparison operators
- `allowAPPROX` - Approximate matching
- `allowNull` / `allowNulls` - Null value handling
- `fractionDigits` - Fraction digits for decimals
- `totalDigits` - Total digits
- `maxExclusive` / `minExclusive` - Exclusive bounds
- `maxInclusive` / `minInclusive` - Inclusive bounds (mentioned but not fully explained)
- `maxLength` / `minLength` - Length constraints (mentioned but not fully explained)
- `pattern` - Pattern matching
- `mask` - Input mask

### Reporting Attributes
- `showInReport` - Whether to show in report
- `displayState` - Display state

### Event & Action Attributes
- `eventName` - Event name
- `action` - Action type
- `targetNames` - Target element names
- `targetItemID` - Target item ID
- `targetItemName` - Target item name
- `targetItemXPath` - Target item XPath

### Code & Terminology Attributes
- `codeMatchEnum` - Code match enumeration
- `hashAlgorithm` - Hash algorithm
- `hashType` - Hash type

### Package Attributes
- `packageID` - Package identifier
- `pkgTitle` - Package title
- `pkgDateTimeStamp` - Package date/time stamp

## Recommendations

1. **Priority 1 - Core Elements**: Document the most commonly used elements:
   - Events (BeforeLoadForm, BeforeShowForm, etc.)
   - Actions (ActivateIf, SetValue, etc.)
   - Response types and data types
   - ListField and ListItem attributes
   - InjectForm functionality

2. **Priority 2 - Important Attributes**: Document critical attributes:
   - All FormDesign instance attributes
   - Selection and activation attributes
   - Data type validation attributes
   - Reporting attributes

3. **Priority 3 - Advanced Features**: Document advanced features:
   - Package management
   - Mapping and terminology
   - Contact and organization structures
   - Rules and expressions

4. **Consider**: Some elements/attributes may be:
   - Deprecated or rarely used
   - Internal implementation details
   - Part of external schemas (XHTML, etc.)
   - Advanced features for specific use cases

## Notes

- Many HTML/XHTML attributes are included in the schema but shouldn't be documented as SDC-specific
- Some elements are part of package management (IDR_Package, etc.) which may be out of scope for basic form design
- The notebook focuses on form design basics; advanced features like rules, expressions, and packages may need separate documentation







CREATE TABLE [dbo].[weather](
	[datecreated] [datetime] NOT NULL DEFAULT (getdate()),
	[info] [varchar](max) NULL
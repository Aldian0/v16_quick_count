{
    "name": "Web Responsive UX",
    "summary": "Custom mod",
    "version": "16.0.1.0.0",
    "category": "Backend Theme",
    "author": "Youring",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["web_responsive"],
    "development_status": "Production/Stable",
    "data": [
    ],
    # v16 change
    "assets": {
        # before for definition change
        "web._assets_primary_variables": [
            ("before", "/web/static/src/scss/primary_variables.scss", "/web_responsive_ux/static/src/scss/primary_variables.scss"),
        ],
        
        "web._assets_secondary_variables": [
            ("before", "/web/static/src/scss/secondary_variables.scss", "web_responsive_ux/static/src/scss/secondary_variables.scss"),
        ],
        
        "web._assets_backend_helpers": [
            ("before", "/web/static/src/scss/bootstrap_overridden.scss", "/web_responsive_ux/static/src/scss/bootstrap_overridden.scss"),
        ],
        
        "web.assets_backend": [
            ("include", "web._assets_backend_helpers"), 
            # core override
            "/web_responsive_ux/static/src/core/**/*",
            "/web_responsive_ux/static/src/search/**/*",
            "/web_responsive_ux/static/src/views/**/*",
            # web_responsive override
            "/web_responsive_ux/static/src/components/**/*",
            "/web_responsive_ux/static/src/legacy/scss/web_responsive_ux.scss",
            
        ],
    },
    "sequence": 2,
    "application": True,
}

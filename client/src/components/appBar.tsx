import React from 'react';
import { AppBar as MuiAppBar, Toolbar, Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(() => ({
    appBar: {
        background: "#000",
    }
}));

interface MainProps { }



const AppBar = (props: React.PropsWithChildren<MainProps>) => {
    const classes = useStyles()

    return (
        <div>
            <MuiAppBar
                className={classes.appBar}
                color="primary"
            >
                <Toolbar>
                    <Typography variant="h5" color="secondary">
                        GeoJsonLD
                    </Typography>
                </Toolbar>
            </MuiAppBar>
            <Toolbar />
        </div>
    );
}

export { AppBar }
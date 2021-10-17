import React from 'react';
import { Grid, Typography } from '@material-ui/core';

interface ErrorContainerProps {
    error: any
}

const ErrorContainer = (props: React.PropsWithChildren<ErrorContainerProps>) => {
    const { error } = props;

    if (!error) {
        return null;
    }

    return (
        <Grid container direction="column" alignItems="center" spacing={4} style={{ width: "100%" }} >
            <Grid item>
                <Typography color="error" variant="h5">
                    Could not produce JSON-LD successfully
                </Typography>
            </Grid>
            <Grid item>
                <Typography color="error" variant="h6">
                    {error}
                </Typography>
            </Grid>
        </Grid>
    );
}

export { ErrorContainer }
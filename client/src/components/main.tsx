import React from 'react';
import { CircularProgress, Grid, makeStyles, Typography } from '@material-ui/core';
import { AppBar } from './appBar';
import { getUrl } from '../appServices';
import { RequestFormType } from '../requestForm';
import { RequestForm } from './requestForm';

const useStyles = makeStyles(() => ({
    root: {
        height: "100vh"
    },
    requestForm: {
        height: "90vh"
    }

}));

interface MainProps { }

const Main = (props: React.PropsWithChildren<MainProps>) => {
    const [error, setError] = React.useState(null);
    const [loading, setLoading] = React.useState(false);
    const [result, setResult] = React.useState(null);

    const classes = useStyles();

    const handleonClick = (requestForm: RequestFormType) => {
        setLoading(true);
        setResult(null);

        fetch(getUrl(requestForm.id), {
            method: 'POST',
            cache: "no-cache",
            body: JSON.stringify({ username: requestForm.username, password: requestForm.password }),
            headers: new Headers({
                'mode': 'cors',
                'Content-Type': 'application/json'
            })
        })
            .then(
                (result) => {
                    const jsonResult = result.json()
                    console.log("result " + jsonResult);
                    return jsonResult;
                },
                (error) => {
                    console.log("Error" + error);
                    setLoading(false);
                    setError(error);
                }
            )
            .then(
                // TODO: Fix loading remaining true after error response
                (data) => {
                    setLoading(false);
                    setResult(data);
                    console.log(data)
                }
            )
    }

    return (
        <div>
            <Grid container className={classes.root} justify="center">
                <Grid item xs={12}>
                    <AppBar />
                </Grid>
                <Grid item container className={classes.requestForm} justify="center" alignItems="center" xs={10}>
                    <Grid item xs={5}>
                        <RequestForm
                            loading={loading}
                            submitRequest={handleonClick}
                        />
                    </Grid>
                    <Grid item container justify="center" alignItems="center" xs={5}>
                        <Grid item>
                            {result &&
                                <pre>
                                    {JSON.stringify(result, null, '\t')}
                                </pre>
                            }
                            {
                                loading && <CircularProgress size={60} color="secondary" />
                            }
                            <Typography color="error">
                                {error && error.message}
                            </Typography>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
        </div>
    );
}

export { Main }
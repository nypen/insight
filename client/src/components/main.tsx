import React from 'react';
import { Grid, LinearProgress, makeStyles, Typography } from '@material-ui/core';
import { AppBar } from './appBar';
import { getUrl } from '../appServices';
import { RequestFormType } from '../requestForm';
import { RequestForm } from './requestForm';

const useStyles = makeStyles(() => ({
    root: {
        border:"3px solid #66afff",
        height: "100vh"
    },
    requestForm: {
        border:"3px solid #66a5a3",
        height: "500px"
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
                    console.log(result);
                    return result.json();
                },
                (error) => {
                    console.log("Error" + error);
                    setLoading(false);
                    setError(error);
                }
            )
            .then(
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
                <Grid item container className={classes.requestForm} xs={10}>
                    <Grid item xs={5}>
                        <RequestForm
                            loading={loading}
                            submitRequest={handleonClick}
                        />
                    </Grid>
                    <Grid item container justify="center" alignItems="center" xs={5}>
                        <pre>
                            {JSON.stringify(result, null, '\t')}
                        </pre>
                        {
                            loading && <LinearProgress color="secondary" />
                        }
                        <Typography color="error">
                            {error && error.message}
                        </Typography>
                    </Grid>
                </Grid>
            </Grid>
        </div>
    );
}

export { Main }